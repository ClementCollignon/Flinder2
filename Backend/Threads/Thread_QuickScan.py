# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import cv2
import os
import time

class Thread_QuickScan(QThread):
    signal_update_stage = pyqtSignal()
    signal_quickscan_end = pyqtSignal()
    
    def __init__(self, variables, scan_gain = 1000, scan_exposure = 0.1, wafer_threshold = 50, sleep_time = 0.4):
        super(Thread_QuickScan, self).__init__()
        
        self.stop = False
        
        self.sleep_time = sleep_time
        self.scan_gain = scan_gain
        self.scan_exposure = scan_exposure
        self.wafer_threshold = wafer_threshold
        
        
        self.variables = variables
        self.my_scope = self.variables.my_scope
        self.step_size = self.variables.get_step_size()
        self.square_size = self.variables.get_square_size()
        
        
    def run(self):
        x0, y0 = self.prepare_scope()
        pos_list = self.create_position_list(x0, y0)
                
        self.scan_stage(x0, y0, pos_list)
        self.reset_exposure()
        self.signal_quickscan_end.emit()
    
    def prepare_scope(self):
        self.my_scope.camera.bin_image()
        self.my_scope.stage.initialise_stage()
        self.my_scope.stage.set_as_origin()
        self.my_scope.stage.set_as_origin()
        x0, y0 = self.my_scope.stage.get_stage_position_xy()
        
        self.exposure = self.my_scope.camera.get_exposure()
        self.gain = self.my_scope.camera.get_gain()
        
        self.my_scope.camera.set_exposure(self.scan_exposure)
        self.my_scope.camera.set_gain(self.scan_gain)
        
        return x0, y0
    
    def create_position_list(self, x0, y0):
        y_range, x_range = self.variables.get_stage_area()
        x_range*=1000
        y_range*=1000
        
        nsteps_x = int(x_range/self.step_size) + 1
        nsteps_y = int(y_range/self.step_size) + 1
        
        pos_list = []
        
        for i in range(nsteps_x):
            for j in range(nsteps_y):
                
                if i%2 == 0:
                    alpha = -j*self.step_size
                else:
                    alpha = y0 - (nsteps_y - 1)*self.step_size + j*self.step_size
                
                pos_list.append([x0-i*self.step_size,y0+alpha])
        return pos_list
    
    def scan_stage(self, x0, y0, pos_list):  
        for xy in pos_list:
            self.my_scope.stage.set_stage_position_xy(xy[0], xy[1])
            time.sleep(self.sleep_time)
            image = self.my_scope.camera.snap_image()
            
            
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.rotate(image, cv2.ROTATE_180)
            image = cv2.resize(image, (self.square_size,self.square_size))
            
            image[image>self.wafer_threshold] = 255
            image[image<=self.wafer_threshold] = 0
            
            jj = int(-xy[0]/self.step_size)
            ii = int(-xy[1]/self.step_size)
            
            
            self.variables.set_mat_stage(ii*self.square_size, jj*self.square_size, image)
            
            self.variables.set_mat_stage_xy(ii*self.square_size,jj*self.square_size,self.square_size, xy)
            
            self.signal_update_stage.emit()
            
            if self.stop:
                break
            
        mat = self.variables.get_mat_stage()
        cv2.imwrite(self.variables.get_working_folder()+"/wafers_position.jpg", mat)
    
    def reset_exposure(self):
        self.my_scope.camera.set_exposure(self.gain)
        self.my_scope.camera.set_gain(self.exposure)
    
    def kill(self):
        self.stop = True

class Thread_Identify_Wafers(QThread):
    signal_idwafers_end = pyqtSignal()
    
    def __init__(self, variables):
        QThread.__init__(self)
        
        self.FONT = cv2.FONT_HERSHEY_SIMPLEX
        self.FONT_SCALE = 20
        self.FONT_THICKNESS = 70
        self.BLACK_COLOR = (0,0,0)
        self.WHITE_COLOR = (255,255,255)
        self.WAFER_NUMBER_COLOR = (129,178,154)
        
        self.variables = variables
        
        self.mat_stage = self.get_mat_stage()
        self.h, self.w = self.mat_stage.shape
        
    def run(self):
        large_contours = self.find_large_contours()
        self.draw_wafer_numbers(large_contours)
        self.create_folders(large_contours)
        self.signal_idwafers_end.emit()
    
    def get_mat_stage(self):
        mat_stage = self.variables.get_mat_stage()
        mat_stage = cv2.cvtColor(mat_stage, cv2.COLOR_GRAY2RGB)
        return mat_stage
    
    def find_large_contours(self):
        contours, hierarchy = cv2.findContours(self.mat_stage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        large_contours = []
        for i,contour in enumerate(contours):
            if cv2.contourArea(contour) > 1e6:
                contour = cv2.approxPolyDP(contour,0.005*cv2.arcLength(contour,True),True)
                contour = cv2.convexHull(contour)
                cv2.drawContours(self.mat_stage, [contour], -1, (255,255,255), thickness=cv2.FILLED)
                large_contours.append(contour)
                self.variables.set_wafer_contour(i,contour)
        
        return large_contours
    
    def draw_wafer_numbers(self,large_contours):
        mask = np.zeros((self.h, self.w, 3), dtype = np.uint8)
        cv2.drawContours(mask, large_contours, -1, (120,120,120), thickness=cv2.FILLED)
        
        for wafer_number, contour in enumerate(large_contours):
            rect = cv2.minAreaRect(contour)
            position = (int(rect[0][0]),int(rect[0][1]))
            text = str(wafer_number)
            
            textsize = cv2.getTextSize(text, self.FONT, self.FONT_SCALE, self.FONT_THICKNESS)[0]
            tupple_position=(int(position[0] - textsize[0]/2),int(position[1] + textsize[1]/2))
            
            cv2.putText(mask ,text , tupple_position, self.FONT, self.FONT_SCALE, self.WAFER_NUMBER_COLOR, self.FONT_THICKNESS)
        
        self.variables.set_mat_stage_id(mask)
        
        cv2.imwrite(self.variables.get_working_folder()+"/wafers_position_id.jpg", mask)
        
    
    def create_folders(self, large_contours):
        for wafer_number, contour in enumerate(large_contours):
            try:
                os.mkdir(self.variables.get_working_folder()+f"/Wafer{wafer_number}")
            except:
                print("folder already exists")
            
class Thread_Prepare_SlowScan(QThread):
    signal_end = pyqtSignal()
    
    def __init__(self, variables):
        QThread.__init__(self)
        
        self.variables = variables
        
        self.mat_stage = self.get_mat_stage()
        self.h, self.w = self.mat_stage.shape
        
        self.quick_scan_step = self.variables.get_step_size() # um
        self.square_size = self.variables.get_square_size() # px
        self.stage_px_size = self.quick_scan_step / self.square_size # um/px
        
        self.field_of_view = self.variables.get_field_of_view()
        
        self.overlap = self.variables.get_overlap_percent()/100
        
        self.translate_x = self.field_of_view[0]*(1-self.overlap)/self.stage_px_size #um
        self.translate_y = self.field_of_view[1]*(1-self.overlap)/self.stage_px_size #um
        
        self.margin = int(self.quick_scan_step/self.stage_px_size/2) #px
        
        self.num_focus_points = self.variables.get_num_focus_points()
        
        self.wafers_contours = self.variable.get_wafers_contours()
        
        limit_fov = self.field_of_view[0] / self.stage_px_size / 2
        limit_step_size = self.quick_scan_step / self.stage_px_size / 2
        self.limit_um = limit_fov + limit_step_size
        
    def run(self):
        for wafer_number in self.wafers_contours:
           contour = self.wafers_contours[wafer_number]
           xmin, xmax, ymin, ymax = self.get_bounding_rectangle(contour)
           position_list, focus_list = self.create_position_list(contour,
                                                                 xmin, xmax,
                                                                 ymin, ymax)
           
           self.variables.set_xy_scan_positions(wafer_number, position_list)
           self.variables.set_xy_focus_positions(wafer_number, focus_list)
        
        self.signal_end.emit()
    
    def get_bounding_rectangle(self, contour):
        x,y,width,height = cv2.boundingRect(contour)
        
        xmin = max(x-self.margin,0)
        ymin = max(y-self.margin,0)
        xmax = min(x+width+self.margin,self.w)
        ymax = min(y+height+self.margin,self.h)
        
        return xmin, xmax, ymin, ymax
    
    def is_close_to_wafer(self, contour, coordinates):
        return cv2.pointPolygonTest(contour, coordinates, True) > -self.limit_um
    
    def is_in_wafer(self, contour, coordinates):
        return cv2.pointPolygonTest(contour, coordinates, True) > 0
    
    def append_position(self,positions,coordinates):
        x = coordinates[0]*self.stage_px_size
        y = coordinates[1]*self.stage_px_size
        positions.append(x,y)
        return positions
    
    def select_focus_points(self, focus_list):
        N = len(focus_list)
        i=0
        indices = []
        while i < self.num_focus_points:
            ii = np.random.randint(0,N)
            if ii not in indices:
                indices.append(ii)
                i+=1
        
        indices = np.asarray(indices)
        focus_list = np.asarray(focus_list)
        indices = np.sort(indices)
        
        return focus_list[indices]
    
    def create_position_list(self, contour, xmin, xmax, ymin, ymax):
        X = xmin
        Y = ymin
        
        position_list = []
        focus_list = []
        
        while Y <= ymax:  
            while X <= xmax:
                X+=self.translate_x
                if self.is_close_to_wafer(contour, (X,Y)):
                    position_list = self.append_position(position_list, (X,Y))
                if self.is_in_wafer(contour, (X,Y)):
                    focus_list = self.append_position(focus_list, (X,Y))
            Y+=self.translate_y
            
            while X >= xmin:
                X-=self.translate_x
                if self.is_close_to_wafer(contour, (X,Y)):
                    position_list = self.append_position(position_list, (X,Y))
                if self.is_in_wafer(contour, (X,Y)):
                    focus_list = self.append_position(focus_list, (X,Y))
            Y+=self.translate_y
        
        focus_list = self.select_focus_points(focus_list)
        
        return position_list, focus_list
        
        
            
            
            
            
            
            
            
            
                
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
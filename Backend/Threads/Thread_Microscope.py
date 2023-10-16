# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from numpy import round
import numpy as np
import cv2
import os
import time
import sys

from PyQt5.QtGui import QImage, QPixmap

class Thread_Quick_Scan(QThread):
    updateStageSignal = pyqtSignal()
    
    def __init__(self, resolution_scaling, variables):
        QThread.__init__(self)
        self.resolution_scaling = resolution_scaling
        self.variables = variables
        
        self.stop = False
        self.my_scope = self.variables.my_scope
        self.step_size = self.variables.get_step_size()
        self.square_size = int(self.step_size / 10)
        
    def run(self):
        x0, y0 = self.prepare_scope()
        pos_list = self.create_position_list(x0, y0)
        size, pad_w, pad_h = self.get_padding(self.square_size)
        self.scan_stage(x0, y0, pos_list, size, pad_h, pad_w)
    
    def prepare_scope(self):
        self.my_scope.camera.bin_image()
        self.my_scope.stage.initialise_stage()
        self.my_scope.stage.set_as_origin()
        self.my_scope.stage.set_as_origin()
        x0, y0 = self.my_scope.stage.get_stage_position_xy()
        
        self.exposure = self.my_scope.camera.get_exposure()
        self.gain = self.my_scope.camera.get_gain()
        
        self.my_scope.camera.set_exposure(0.1)
        self.my_scope.camera.set_gain(1000)
        
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
    
    def get_padding(self, square_dimension):
        pixel_size = self.my_scope.get_pixel_size()
                
        image = self.my_scope.camera.snap_image()
        height, width, ch = image.shape
        
        size = ( (int(width*pixel_size/10)//2)*2 , (int(height*pixel_size/10)//2)*2 )
        
        pad_w = int((square_dimension-size[0])/2)
        pad_h = int((square_dimension-size[1])/2)
        
        return size, max(pad_w, 0), max(pad_h, 0)
        
    
    def scan_stage(self, x0, y0, pos_list, size, pad_h, pad_w):  
        for xy in pos_list:
            self.my_scope.stage.set_stage_position_xy(xy[0], xy[1])
            time.sleep(0.4)
            image = self.my_scope.camera.snap_image()
            
            
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.rotate(image, cv2.ROTATE_180)
            image = cv2.resize(image, size)
            
            image = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_REPLICATE)

            image[image>50] = 255
            image[image<=50] = 0
            
            jj = int(-xy[0]/self.step_size)
            ii = int(-xy[1]/self.step_size)
            
            
            self.variables.set_mat_stage(ii*self.square_size, jj*self.square_size, image)
            
            self.variables.set_mat_stage_xy(ii*self.square_size,jj*self.square_size,self.square_size, xy)
            
            self.updateStageSignal.emit()
            
            if self.stop:
                break
            
        mat = self.variables.get_mat_stage()
        cv2.imwrite(self.variables.get_working_folder()+"/wafers_position.jpg", mat)
        
    def kill(self):
        self.stop = True

class Thread_Identify_Wafers(QThread):
    identifyWafersSignal = pyqtSignal()
    
    def __init__(self, resolution_scaling, variables):
        QThread.__init__(self)
        
        self.variables = variables
        self.resolution_scaling = resolution_scaling
        
        self.FONT = cv2.FONT_HERSHEY_SIMPLEX
        self.FONT_SCALE = 20
        self.FONT_THICKNESS = 70
        self.BLACK_COLOR = (0,0,0)
        self.WHITE_COLOR = (255,255,255)
        self.WAFER_NUMBER_COLOR = (129,178,154)
        
        self.mat_stage = self.get_mat_stage()
        self.h, self.w = self.mat_stage.shape
        
    def run(self):
        large_contours = self.find_large_contours()
        self.draw_wafer_numbers(large_contours)
        self.create_folders(large_contours)
        self.identifyWafersSignal.emit()
    
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


class Thread_Cam(QThread):
    changePixmap = pyqtSignal(QImage)
    
    def __init__(self, resolution_scaling, my_scope):
        QThread.__init__(self)
        self.resolution_scaling = resolution_scaling
        self.isOpen = True
        self.my_scope = my_scope
        
    def run(self):
        self.my_scope.camera.bin_image()
        while self.isOpen:
            Image  = cv2.rotate(self.my_scope.camera.snap_image(),cv2.ROTATE_180)
            h, w, ch = Image.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(Image.data, w, h, bytesPerLine, QImage.Format_RGB888)
           
            size = self.resolution_scaling.get_display_size_cam()
           
            p = convertToQtFormat.scaled(size, size, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
    
    def kill(self):
        self.isOpen = False

class Thread_Wait_Stage(QThread):
    stageArrived = pyqtSignal()
    
    def __init__(self, my_scope):
        QThread.__init__(self)
        self.my_scope = my_scope
        
    def run(self):
        self.my_scope.stage.initialise_stage()
        self.stageArrived.emit()

class Thread_Stage_GoTo(QThread):
    stageArrivedRef = pyqtSignal()
    
    def __init__(self,my_scope,posX,posY):
        QThread.__init__(self)
        self.my_scope = my_scope
        self.X = posX
        self.Y = posY
        
    def run(self):
        self.my_scope.stage.set_stage_position_xy(self.X,self.Y)
        self.my_scope.stage.wait_stage_xy()
        self.stageArrivedRef.emit()

class Thread_Exposure_1(QThread):
    exposureDone = pyqtSignal()
    
    def __init__(self, my_scope):
        QThread.__init__(self)
        self.my_scope = my_scope
        
    def run(self):
        self.my_scope.stage.set_stage_position_xy(-1087, -360)
        self.my_scope.stage.wait_stage_xy()
        
        for i in range(3):
            self.my_scope.camera.auto_exposure()
            self.my_scope.camera.auto_white()
        self.my_scope.camera.compute_white_balance_coefficient()
        self.exposureDone.emit()

class Thread_Autofocus(QThread):
    autofocusDone = pyqtSignal()
    
    def __init__(self, my_scope):
        QThread.__init__(self)
        self.my_scope = my_scope
        
    def run(self):
        self.my_scope.auto_focus(5000,20)
        self.my_scope.auto_focus(500,10)
        self.my_scope.fine_focus(50,10)
        self.autofocusDone.emit()
        
class Thread_Fast_Bkg(QThread):
    fastBkgDone = pyqtSignal()
    
    def __init__(self, my_scope, variables):
        QThread.__init__(self)
        self.my_scope = my_scope
        self.variables = variables
        
    def run(self):
        # self.my_scope.camera.full_resolution()
        
        x,y, = -1087, -600
        
        dxy=[-400,-200,0,200,400]
        N = len(dxy)
        xy = []
        for i in range(N):
            for j in range(N):
                xy.append([x+dxy[i],y+dxy[j]])
        
        Image = []
        for pos in xy:
            self.my_scope.stage.set_stage_position_xy(pos[0],pos[1])
            time.sleep(0.2)
            
            image = self.my_scope.camera.snap_image()
            image = self.my_scope.camera.color_correct(image)
            Image.append(image)
        
        h,w,px = Image[0].shape
        number_of_pictures = len(Image)
        
        B=np.zeros((h,w,number_of_pictures),dtype=np.uint8)
        G=np.zeros((h,w,number_of_pictures),dtype=np.uint8)
        R=np.zeros((h,w,number_of_pictures),dtype=np.uint8)
                
        for i,image in enumerate(Image):
            r,g,b = cv2.split(image)
            B[:,:,i]=b
            G[:,:,i]=g
            R[:,:,i]=r

        new_b=np.zeros((h,w),dtype=np.uint16)
        new_g=np.zeros((h,w),dtype=np.uint16)
        new_r=np.zeros((h,w),dtype=np.uint16)
                
        np.median(B,axis=2,out=new_b)
        np.median(G,axis=2,out=new_g)
        np.median(R,axis=2,out=new_r)    
        
        bkg = cv2.merge((new_r,new_g,new_b))
        resized = cv2.resize(bkg, (w*3, h*3), interpolation = cv2.INTER_AREA)
        cv2.imwrite("current_bkg.jpg", resized)
        
        self.variables.set_fast_bkg(bkg)
        
        self.fastBkgDone.emit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
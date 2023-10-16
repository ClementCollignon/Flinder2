# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
from scipy.optimize import curve_fit
import cv2
import time

class Thread_FocusPlane(QThread):
    signal_end = pyqtSignal()
    signal_killed = pyqtSignal()
    
    def __init__(self, variables, wafer_number, sleep_time = 0.4, percent_remove = 0.35):
        super(Thread_FocusPlane, self).__init__()
        
        self.stop = False
        
        self.sleep_time = sleep_time
        
        self.variables = variables
        self.my_scope = self.variables.my_scope
        self.wafer_number = wafer_number
        
        self.percent_remove = percent_remove
        
    def run(self):
        
        focus_points = self.get_focus_points()
        
        xyz, sharpness_score = self.focus_routine_loop(focus_points)
        
        if not self.stop:
            xyz = self.remove_bad_points(xyz, sharpness_score)
            plane_parameters = self.fit_plane(xyz)
        
        if not self.stop:
            self.save_plane_parameters(plane_parameters)
            self.signal_end.emit()

        if self.stop:
            self.signal_killed.emit()

    def focus_routine_loop(self, focus_points):
        xyz = []
        sharpness_score_array = []
        for point in focus_points:
            if self.stop:
                break
            x, y = point
            z, sharpness_score = self.focus_routine(x, y)
            xyz.append((x,y,z))
            sharpness_score_array.append(sharpness_score)
        
        return xyz, sharpness_score_array
        
    def save_plane_parameters(self, parameters):
        self.variables.set_plane_parameters(parameters, self.wafer_number)
    
    def plane(self,coord,a,b,c):
        return a*coord[0]+b*coord[1]+c
    
    def fit_plane(self, xyz):
        x,y = xyz[:,0], xyz[:,1]
        X,Y = np.meshgrid(x,y)
        xy = np.vstack((X.ravel(), Y.ravel()))
        z = xyz[:,2]
        
        guess_c = np.mean(z)
        
        popt, pcov = curve_fit(self.plane, xy, z, [0,0,guess_c], maxfev=10000)
    
        return popt
    
    def remove_bad_points(self, xyz, sharpness_score):
        xyz = np.asarray(xyz)
        sharpness_score = np.asarray(sharpness_score)
        
        xyz = xyz[np.argsort(sharpness_score)]
        points_to_remove = int(self.percent_remove*len(xyz)/100)
        
        return xyz[points_to_remove::]
    
    def get_focus_points(self):
        all_focus_points = self.variables.get_xy_focus_positions()
        return all_focus_points[self.wafer_number]
    
    def focus_routine(self, x, y):
        self.my_scope.stage.set_stage_position_xy(x, y)
        self.my_scope.stage.wait_stage_xy()
        
        micron_range = 1000
        number_of_steps = 20
        self.my_scope.camera.auto_focus(micron_range, number_of_steps)
        
        micron_range = 100
        number_of_steps = 20
        self.my_scope.camera.fine_focus(micron_range, number_of_steps)
        
        micron_range = 10
        number_of_steps = 20
        z, sharpness_score = self.my_scope.camera.fine_focus(micron_range,
                                                             number_of_steps)
        
        return z, sharpness_score
        
    def kill(self):
        self.stop = True

            
class Thread_SlowScan(QThread):
    signal_end = pyqtSignal()
    signal_enough_pictures = pyqtSignal()
    
    def __init__(self, variables, wafer_number, sleep_time = 0.4):
        super(Thread_SlowScan, self).__init__()
        
        self.stop = False
        
        self.sleep_time = sleep_time
        
        self.variables = variables
        self.my_scope = self.variables.my_scope
        self.wafer_number = wafer_number
        
        self.pictures_taken = 0
        self.color_correct_trigger = 50
        
    def run(self):
        self.my_scope.camera.full_resolution()
        x,y,z = self.get_scan_coordinates()        
        self.scan_routine_loop(x,y,z)
    
    def scan_routine_loop(self,x_array, y_array, z_array):
        self.total_number_pic = len(x_array)
        self.n_zeros = len(str(self.total_number_pic))
        for x, y, z in zip(x_array, y_array, z_array):
            self.check_color_correct()
            self.scan_routine(x, y, z)
    
    def check_color_correct(self):
        condition1 = ( self.pictures_taken == self.color_correct_trigger )
        condition2 = ( self.pictures_taken == self.total_number_pic )
        if condition1 or condition2 :
            self.signal_enough_pictures.emit()
        self.pictures_taken+=1
    
    def scan_routine(self, x, y, z, averaging = 1):
        self.my_scope.stage.set_stage_position_xy(x, y)
        self.my_scope.stage.set_stage_position_z(z)
        self.wait_stage_xy()
        self.wait_stage()
        time.sleep(self.sleep_time)
        image = self.take_picture(averaging)
        self.save_picture(image)
    
    def save_picture(self, image):
        folder_path = self.variables.get_working_folder()
        pic_number = str(self.pictures_taken).zfill(self.n_zeros)
        wafer_number = str(self.wafer_number).zfill(2)
        path = (f"{folder_path}/"
                f"wafer_{wafer_number}/"
                f"pictures/"
                f"pic_{pic_number}.png")
        compression = [cv2.IMWRITE_PNG_COMPRESSION, 0]
        cv2.imwrite(path, image, compression)
        
    def take_picture(self, averaging):
        snap = self.my_scope.camera.snap_image()
        if averaging == 1:
            return snap
        
        image = snap.astype(np.float)
        for i in range(averaging):
            snap = self.my_scope.camera.snap_image()
            image += snap.astype(np.float)
            time.sleep(self.sleep_time)
        
        image = np.round(image/averaging, decimals = 0)
        
        return image.astype(np.uint8)
        
    
    def get_scan_coordinates(self):
        all_coordinates = self.variables.get_xy_scan_positions()
        xy = all_coordinates[self.wafer_number]
        x = xy[:,0]
        y = xy[:,1]
        
        #a, b, c are the plane parameters
        a, b, c = self.variables.get_plane_parameters(self.wafer_number)
        
        z = a*x + b*y + c
        
        return x, y, z
    
    def kill(self):
        self.stop = True          
            
            
            
            
                
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
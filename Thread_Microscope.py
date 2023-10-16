# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from numpy import round
import numpy as np
import cv2
import os
import time

from PyQt5.QtGui import QImage, QPixmap

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
        print(self.my_scope.stage.get_stage_position_xy())
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
        self.my_scope.auto_focus(5000,10)
        self.my_scope.auto_focus(500,10)
        #self.my_scope.fine_focus(50,10)
        self.autofocusDone.emit()
        
class Thread_Fast_Bkg(QThread):
    fastBkgDone = pyqtSignal()
    
    def __init__(self, my_scope, backend):
        QThread.__init__(self)
        self.my_scope = my_scope
        self.backend = backend
        
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
        
        self.backend.variables.set_fast_bkg(bkg)
        
        self.fastBkgDone.emit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
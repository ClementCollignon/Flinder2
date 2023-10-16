# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap

class Thread_Convert_Image(QThread):
    signal_QImage = pyqtSignal(QImage)
    
    def __init__(self, size, image, h = 0, w = 0, ch = 0):
        super(Thread_Convert_Image, self).__init__()
        self.image = image
        self.size = size
        
        self.h = h
        self.w = w
        self.ch = ch
        
    def run(self):
        
        if self.h == 0 or self.w == 0 or self.ch == 0:
            self.h, self.w, self.ch = self.get_shape()
        
        bytesPerLine = self.ch * self.w
        
        color = self.get_color()
        
        convertToQtFormat = QImage(self.image.data, self.w, self.h, bytesPerLine, color)
        image = convertToQtFormat.scaled(self.size[0],self.size[1], Qt.KeepAspectRatio)
        
        self.signal_QImage.emit(image)
    
    def get_shape(self):
        shape = self.image.shape
        if len(shape) == 2:
            h,w = shape
            ch = 1
            return h,w,ch
        return shape
    
    def get_color(self):
        if self.ch == 1:
            return QImage.Format_Grayscale8
        return QImage.Format_RGB888
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
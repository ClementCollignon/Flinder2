# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from Style.GUI_Object import SmallButton
from PyQt5.QtCore import pyqtSlot, QTimer

import cv2

class Load_Picture(QtWidgets.QMainWindow):
    def __init__(self, resolution_scaling):
        super(Load_Picture, self).__init__()
        self.setObjectName("PopWindow")
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        
        self.resolution_scaling = resolution_scaling
        
        width,height = self.resolution_scaling.get_popup_initialise_stage_size()
        self.resize(width,height)
        
        self.setup_ui()
        
        self.connect_buttons()
        
        self.retranslate_popup()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    
    def setup_ui(self):        
        self.central_widget = QtWidgets.QWidget(self)
        
        self.horizontal_layout_master = QtWidgets.QHBoxLayout(self.central_widget)
        margin = self.resolution_scaling.get_margin_popup_initialise_stage()
        self.horizontal_layout_master.setContentsMargins(margin, margin, margin, margin)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_master.addItem(spacerItem)
        
        picture = self.setup_picture()
        self.horizontal_layout_master.addItem(picture)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_master.addItem(spacerItem)
        
        self.setCentralWidget(self.central_widget)
        
        self.retranslate_popup()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    
    def setup_picture(self):
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.label_picture = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_0.addWidget(self.label_picture)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        return horizontal_layout_0
    
    def display_picture(self):
        
        image = cv2.imread("pic60.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        h, w, ch = image.shape
        bytesPerLine = ch * w
        
        sizew, sizeh = int(w/2), int(h/2)
        
        convertToQtFormat = QtGui.QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)
        
        convertToQtFormat = convertToQtFormat.scaled(sizew, sizeh, QtCore.Qt.KeepAspectRatio)
        
        self.label_picture.setPixmap(QtGui.QPixmap.fromImage(convertToQtFormat))
    
    def connect_buttons(self):
        pass
    
    def retranslate_popup(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PopWindow", "Calibration"))
        self.display_picture()
        
        
        
    
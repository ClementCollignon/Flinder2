# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from Style.GUI_Object import Sizes

class Ui_Tab(object):
    def __init__(self, icon, variables):
        self.tab_number = self.define_tab_number()
        self.tab_names = ["Scan", "Hunt", "Zoom-In", "Create\n  Calibration", "Train AI", "Options"]
        self.icon = icon.icons_tab[self.tab_number]
        self.variables = variables
    
    def define_tab_number(self):
        return 0
        
    def setup_ui(self, MainWindow):
        self.resolution_scaling = Sizes() 
        
        self.central_widget = QtWidgets.QWidget(MainWindow)
        
        self.horizontal_layout_master = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontal_layout_master.setContentsMargins(0, 0, 0, 0)
        
        self.left_tabs_widget = self.setup_left_tabs_ui()
        self.horizontal_layout_master.addWidget(self.left_tabs_widget)
        
        item = self.setup_right_window_ui()
        self.horizontal_layout_master.addItem(item)
        
        self.horizontal_layout_master.setStretch(0, 20)
        self.horizontal_layout_master.setStretch(1, 100)
        
        MainWindow.setCentralWidget(self.central_widget)
        
        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.connect_buttons()
    
    def setup_left_tabs_ui(self):
        left_tabs_widget = QtWidgets.QListWidget(self.central_widget)
        left_tabs_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        
        for i in range(len(self.tab_names)):
            item = QtWidgets.QListWidgetItem()
            left_tabs_widget.addItem(item)

        return left_tabs_widget
    
    def setup_right_window_ui(self):
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        return spacerItem
    
    def retranslate_ui(self,MainWindow):
        self.retranslate_left_tabs_ui(MainWindow)
        self.retranslate_right_window_ui(MainWindow)
    
    def retranslate_left_tabs_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.left_tabs_widget.isSortingEnabled()
        self.left_tabs_widget.setSortingEnabled(False)
        
        for i in range(len(self.tab_names)):
            item = self.left_tabs_widget.item(i)
            item.setText(_translate("MainWindow", "  "+self.tab_names[i]))
            item.setIcon(self.icon[i])
        self.left_tabs_widget.setSortingEnabled(__sortingEnabled)
        
        icon_pixel_size = self.resolution_scaling.get_icon_tab_size()
        self.left_tabs_widget.setIconSize(QtCore.QSize(icon_pixel_size, icon_pixel_size))
    
    def retranslate_right_window_ui(self,MainWindow):
        pass

    def connect_buttons(self):
        pass
        
        

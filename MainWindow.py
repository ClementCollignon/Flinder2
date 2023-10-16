# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Tabs.Scan_Tab import Scan_Tab
from Tabs.Hunt_Tab import Hunt_Tab
from Tabs.Zoom_Tab import Zoom_Tab
from Tabs.Calibration_Tab import Calibration_Tab
from Tabs.AI_Tab import AI_Tab
from Tabs.Option_Tab import Option_Tab

from Style.GUI_Object import Sizes
from Style.Icon import Icon
from Backend.Variables import Variables

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowIcon(QtGui.QIcon('Style/Icon.png'))
        
        self.icon = Icon("Style/Icons")
        
        self.resolution_scaling = Sizes()
        self.variables = Variables()
        
        width,height = self.resolution_scaling.get_window_size()
        self.resize(width,height)
        
        self.displayed_tab = Scan_Tab(self.icon,self.variables)
        
        self.start_tab()

        self.retranslate_main_ui()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    
    def closeEvent(self, event):
        self.variables.my_scope.close_connection()
        event.accept()
    
    def retranslate_main_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Flinder"))
        
    def start_tab(self):
        self.displayed_tab.setup_ui(self)
        self.displayed_tab.left_tabs_widget.setCurrentItem( self.displayed_tab.left_tabs_widget.item(self.displayed_tab.tab_number) )
        self.displayed_tab.left_tabs_widget.itemClicked.connect(self.tab_selector)
        self.show()
    
    def tab_selector(self):
        item_clicked = self.displayed_tab.left_tabs_widget.currentRow()
        if item_clicked == self.displayed_tab.tab_number:
            return None
        if item_clicked == 0:
            self.displayed_tab = Scan_Tab(self.icon,self.variables)
        if item_clicked == 1:
            self.displayed_tab = Hunt_Tab(self.icon,self.variables)
        if item_clicked == 2:
            self.displayed_tab = Zoom_Tab(self.icon,self.variables)
        if item_clicked == 3:
            self.displayed_tab = Calibration_Tab(self.icon,self.variables)
        if item_clicked == 4:
            self.displayed_tab = AI_Tab(self.icon,self.variables)
        if item_clicked == 5:
            self.displayed_tab = Option_Tab(self.icon,self.variables)
        self.start_tab()
        
        
        
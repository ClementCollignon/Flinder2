# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Style.GUI_Object import Title, Informator
from Tabs.Ui_Tab import Ui_Tab

class Zoom_Tab(Ui_Tab):
    def define_tab_number(self):
        return 2
        
    def setup_right_window_ui(self):
        left,right,top,bottom = self.resolution_scaling.get_margin_main_window()
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(left,right,top,bottom)
        spacing = self.resolution_scaling.get_hspacing_right_window()
        horizontal_layout_0.setSpacing(spacing)
        
        #item 1
        left_pannel = self.setup_left_pannel()
        horizontal_layout_0.addItem(left_pannel)
        
        #item 2
        middle_line = QtWidgets.QFrame(self.central_widget)
        middle_line.setFrameShape(QtWidgets.QFrame.VLine)
        middle_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        horizontal_layout_0.addWidget(middle_line)
        
        #item 3
        right_pannel = self.setup_right_pannel()
        horizontal_layout_0.addItem(right_pannel)
        
        #relative strech of items
        horizontal_layout_0.setStretch(0, 90)
        horizontal_layout_0.setStretch(1, 1)
        horizontal_layout_0.setStretch(2, 100)
        
        return horizontal_layout_0
        
    
    def setup_left_pannel(self):
        vertical_layout_left = QtWidgets.QVBoxLayout()
        vertical_layout_left.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_left_pannel()
        vertical_layout_left.setSpacing(spacing)
        
        #widget 0
        widget_working_folder = self.setup_working_folder()
        vertical_layout_left.addItem(widget_working_folder)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_left.addWidget(line)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #widget 1
        widget_step1 = self.setup_step1()
        vertical_layout_left.addItem(widget_step1)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_left.addWidget(line)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #widget 2
        widget_scan_options = self.setup_step2()
        vertical_layout_left.addItem(widget_scan_options)
        
        return vertical_layout_left
    
    def setup_right_pannel(self):
        vertical_layout_right = QtWidgets.QVBoxLayout()
        vertical_layout_right.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_left_pannel()
        vertical_layout_right.setSpacing(spacing)
        
        #item 0
        title = self.setup_final_touch_title_widget()
        vertical_layout_right.addItem(title)
        
        #item 1
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 2
        widget_layerID = self.setup_layerID_widget()
        vertical_layout_right.addItem(widget_layerID)
        
        #item 3
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 4
        widget_report = self.setup_report_widget()
        vertical_layout_right.addItem(widget_report)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 6
        widget_clean = self.setup_clean_folder_widget()
        vertical_layout_right.addItem(widget_clean)
        
        #item 7
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        return vertical_layout_right
    
    def setup_working_folder(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_working_folder = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_working_folder)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(spacing)
        
        self.button_browse_folder = QtWidgets.QToolButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_browse_folder)
        
        self.path_window = Informator(self.central_widget,self.resolution_scaling)
        w,h = self.resolution_scaling.get_path_window_size()
        self.path_window.setFixedSize(w, h)
        self.path_window.setAlignment(QtCore.Qt.AlignTop)

        horizontal_layout_1.addWidget(self.path_window)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
        
    def setup_step1(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_step1 = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_step1)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_exposure()
        horizontal_layout_1.setSpacing(spacing)
        
        self.label_exposure_bf50x = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_exposure_bf50x)
        
        self.line_edit_exposure_bf50x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_exposure_line_edit()
        self.line_edit_exposure_bf50x.setFixedWidth(width)
        self.line_edit_exposure_bf50x.setAlignment(QtCore.Qt.AlignRight)
        self.line_edit_exposure_bf50x.setValidator(QtGui.QIntValidator(0, 5000))
        horizontal_layout_1.addWidget(self.line_edit_exposure_bf50x)
        
        self.label_ms_bf_50 = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_ms_bf_50)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_create_macro_bf50x = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_create_macro_bf50x)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_step2(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_step2 = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_step2)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(spacing)
        
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vhspacing_step2()
        grid_layout.setSpacing(spacing)
        
        self.label_exposure_step2 = QtWidgets.QLabel(self.central_widget)
        self.label_gain_step2 = QtWidgets.QLabel(self.central_widget)
        
        self.label_df50x = QtWidgets.QLabel(self.central_widget)
        self.label_bf100x = QtWidgets.QLabel(self.central_widget)
        self.label_df100x = QtWidgets.QLabel(self.central_widget)
        
        self.label_df50x_df = QtWidgets.QLabel(self.central_widget)
        self.label_bf100x_bf = QtWidgets.QLabel(self.central_widget)
        self.label_df100x_df = QtWidgets.QLabel(self.central_widget)
        
        self.line_edit_exposure_df50x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_exposure_line_edit()
        self.line_edit_exposure_df50x.setFixedWidth(width)
        self.line_edit_exposure_df50x.setValidator(QtGui.QIntValidator(0, 5000))
        self.line_edit_exposure_df50x.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_exposure_bf100x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_exposure_line_edit()
        self.line_edit_exposure_bf100x.setFixedWidth(width)
        self.line_edit_exposure_bf100x.setValidator(QtGui.QIntValidator(0, 5000))
        self.line_edit_exposure_bf100x.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_exposure_df100x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_exposure_line_edit()
        self.line_edit_exposure_df100x.setFixedWidth(width)
        self.line_edit_exposure_df100x.setValidator(QtGui.QIntValidator(0, 5000))
        self.line_edit_exposure_df100x.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_gain_df50x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_gain_line_edit()
        self.line_edit_gain_df50x.setFixedWidth(width)
        self.line_edit_gain_df50x.setValidator(QtGui.QIntValidator(0, 64))
        self.line_edit_gain_df50x.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_gain_bf100x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_gain_line_edit()
        self.line_edit_gain_bf100x.setFixedWidth(width)
        self.line_edit_gain_bf100x.setValidator(QtGui.QIntValidator(0, 64))
        self.line_edit_gain_bf100x.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_gain_df100x = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_gain_line_edit()
        self.line_edit_gain_df100x.setFixedWidth(width)
        self.line_edit_gain_df100x.setValidator(QtGui.QIntValidator(0, 64))
        self.line_edit_gain_df100x.setAlignment(QtCore.Qt.AlignRight)
        
        grid_layout.addWidget(self.label_exposure_step2, 0, 2)
        grid_layout.addWidget(self.label_gain_step2, 0, 3)
        grid_layout.addWidget(self.label_df50x, 1, 0)
        grid_layout.addWidget(self.label_bf100x, 2, 0)
        grid_layout.addWidget(self.label_df100x, 3, 0)
        grid_layout.addWidget(self.label_df50x_df, 1, 1)
        grid_layout.addWidget(self.label_bf100x_bf, 2, 1)
        grid_layout.addWidget(self.label_df100x_df, 3, 1)
        
        grid_layout.addWidget(self.line_edit_exposure_df50x, 1, 2)
        grid_layout.addWidget(self.line_edit_exposure_bf100x, 2, 2)
        grid_layout.addWidget(self.line_edit_exposure_df100x, 3, 2)
        grid_layout.addWidget(self.line_edit_gain_df50x, 1, 3)
        grid_layout.addWidget(self.line_edit_gain_bf100x, 2, 3)
        grid_layout.addWidget(self.line_edit_gain_df100x, 3, 3)
        
        horizontal_layout_1.addItem(grid_layout)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_create_macro_step2 = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_create_macro_step2)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        margin = self.resolution_scaling.get_margin_step2()
        spacerItem = QtWidgets.QSpacerItem(0, margin, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        vertical_layout.addItem(spacerItem)
        
        return vertical_layout
    
    def setup_final_touch_title_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.label_final_touch = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.label_final_touch)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout 
    
    def setup_layerID_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_layer_id = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_layer_id)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def setup_report_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_create_report = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_create_report)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_open_report = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_open_report)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
         #relative strech of items
        horizontal_layout.setStretch(0, 10)
        horizontal_layout.setStretch(1, 0)
        horizontal_layout.setStretch(2, 5)
        horizontal_layout.setStretch(3, 0)
        horizontal_layout.setStretch(4, 10)
        
        return horizontal_layout
    
    def setup_clean_folder_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_clean_folder = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_clean_folder)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def retranslate_right_window_ui(self, MainWindow):
        self.retranslate_left_pannel_ui(MainWindow)
        self.retranslate_right_pannel_ui(MainWindow)
        
    def retranslate_left_pannel_ui(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_widget_working_folder_ui(_translate)
        self.retranslate_widget_setup_step1_ui(_translate)
        self.retranslate_widget_setup_step2_ui(_translate)
    
    def retranslate_right_pannel_ui(self,_translate):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_final_widget_ui(_translate)
        self.retranslate_layerID_ui(_translate)
        self.retranslate_report_ui(_translate)
        self.retranslate_clean_folder_ui(_translate)
        
    
    def retranslate_widget_working_folder_ui(self,_translate):
        self.label_working_folder.setText(_translate("MainWindow", "Working Folder"))
        self.button_browse_folder.setText(_translate("MainWindow", "Browse"))
        self.path_window.setText(_translate("MainWindow", "Path: "))

    def retranslate_widget_setup_step1_ui(self, _translate):
        self.label_step1.setText(_translate("MainWindow", "Step 1: 50x"))
        self.label_exposure_bf50x.setText(_translate("MainWindow", "Exposure:  "))
        self.line_edit_exposure_bf50x.setText(_translate("MainWindow", "0"))
        self.label_ms_bf_50.setText(_translate("MainWindow", "ms"))
        self.button_create_macro_bf50x.setText(_translate("MainWindow", " Create Macro "))
    
    def retranslate_widget_setup_step2_ui(self, _translate):
        self.label_step2.setText(_translate("MainWindow", "Step 2: 100x & Dark Field"))
        self.label_exposure_step2.setText(_translate("MainWindow", "Exposure (ms)"))
        self.label_gain_step2.setText(_translate("MainWindow", "Gain"))
        self.label_df50x.setText(_translate("MainWindow", "50x"))
        self.label_bf100x.setText(_translate("MainWindow", "100x"))
        self.label_df100x.setText(_translate("MainWindow", "100x"))
        self.label_df50x_df.setText(_translate("MainWindow", "DF"))
        self.label_bf100x_bf.setText(_translate("MainWindow", "BF"))
        self.label_df100x_df.setText(_translate("MainWindow", "DF"))
        self.line_edit_exposure_df50x.setText(_translate("MainWindow", "2000"))
        self.line_edit_gain_df50x.setText(_translate("MainWindow", "20"))
        self.line_edit_exposure_df100x.setText(_translate("MainWindow", "3000"))
        self.line_edit_gain_df100x.setText(_translate("MainWindow", "30"))
        self.line_edit_exposure_bf100x.setText(_translate("MainWindow", "0"))
        self.line_edit_gain_bf100x.setText(_translate("MainWindow", "0"))
        self.button_create_macro_step2.setText(_translate("MainWindow", " Create Macro "))
    
    def retranslate_final_widget_ui(self, _translate):
        self.label_final_touch.setText(_translate("MainWindow", "Final Touch"))
        
    def retranslate_layerID_ui(self, _translate):
        self.button_layer_id.setText(_translate("MainWindow", " Layer Identification "))
        
    def retranslate_report_ui(self, _translate):
        self.button_create_report.setText(_translate("MainWindow", " Create Report "))
        self.button_open_report.setText(_translate("MainWindow", " Open Report "))
    
    def retranslate_clean_folder_ui(self, _translate):
        self.button_clean_folder.setText(_translate("MainWindow", " Clean Folder "))

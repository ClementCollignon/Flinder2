# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Style.GUI_Object import Title, Informator, ObjectiveButton, MacroButton
from Tabs.Ui_Tab import Ui_Tab

class Option_Tab(Ui_Tab):   
    def define_tab_number(self):
        return 5
        
    def setup_right_window_ui(self):
        left,right,top,bottom = self.resolution_scaling.get_margin_main_window()
        
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(left,right,top,bottom)
        spacing = self.resolution_scaling.get_hspacing_right_window()
        horizontal_layout.setSpacing(spacing)
        
        #item 1
        left_pannel = self.setup_left_pannel()
        horizontal_layout.addItem(left_pannel)
        
        #item 2
        middle_line = QtWidgets.QFrame(self.central_widget)
        middle_line.setFrameShape(QtWidgets.QFrame.VLine)
        middle_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        horizontal_layout.addWidget(middle_line)
        
        #item 3
        right_pannel = self.setup_right_pannel()
        horizontal_layout.addItem(right_pannel)
        
        #relative strech of items
        horizontal_layout.setStretch(0, 90)
        horizontal_layout.setStretch(1, 1)
        horizontal_layout.setStretch(2, 100)
        
        return horizontal_layout
        
    
    def setup_left_pannel(self):
        vertical_layout_main = QtWidgets.QVBoxLayout()
        vertical_layout_main.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_left_pannel()
        vertical_layout_main.setSpacing(spacing)
        
        #item 0
        widget_calibration = self.setup_choose_calibration_folder()
        vertical_layout_main.addItem(widget_calibration)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #item 1
        widget_check_database = self.setup_create_background()
        vertical_layout_main.addItem(widget_check_database)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        return vertical_layout_main
    
    def setup_right_pannel(self):
        vertical_layout_right = QtWidgets.QVBoxLayout()
        vertical_layout_right.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_right_pannel()
        vertical_layout_right.setSpacing(spacing)
        
        #item 0
        title = self.setup_offset_title_widget()
        vertical_layout_right.addItem(title)
        
        #item 1
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 2
        offset_label = self.setup_offset_widget()
        vertical_layout_right.addItem(offset_label)
        
        #item 3
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        vertical_layout_right.setStretch(0, 1)
        vertical_layout_right.setStretch(1, 1)
        vertical_layout_right.setStretch(2, 200)
        vertical_layout_right.setStretch(3, 80)
        
        return vertical_layout_right
    
    def setup_choose_calibration_folder(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_calibration = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_calibration)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(spacing)
        
        self.button_browse_calibration_folder = QtWidgets.QToolButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_browse_calibration_folder)
        
        self.calibration_path_window = Informator(self.central_widget,self.resolution_scaling)
        w,h = self.resolution_scaling.get_calibration_window_size()
        self.calibration_path_window.setFixedSize(w, h)
        self.calibration_path_window.setAlignment(QtCore.Qt.AlignTop)

        horizontal_layout_1.addWidget(self.calibration_path_window)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_create_background(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_create_background = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_create_background)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_nosepiece()
        horizontal_layout_1.setSpacing(spacing)
        
        self.button_5x_background = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_5x_background)
        
        self.button_10x_background = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_10x_background)
        
        self.button_20x_background = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_20x_background)
        
        self.button_50x_background = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_50x_background)
        
        self.button_100x_background = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_100x_background)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        horizontal_layout_2 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_2.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_nosepiece()
        horizontal_layout_2.setSpacing(spacing)
        
        self.label_wafer_type = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_2.addWidget(self.label_wafer_type)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_2.addItem(spacerItem)
        
        self.button_wafer_type = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_2.addWidget(self.button_wafer_type)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_2.addItem(spacerItem)
        
        horizontal_layout_2.setStretch(0, 0)
        horizontal_layout_2.setStretch(1, 1)
        horizontal_layout_2.setStretch(2, 0)
        horizontal_layout_2.setStretch(3, 5)
        
        vertical_layout.addItem(horizontal_layout_2)
        
        
        horizontal_layout_3 = QtWidgets.QHBoxLayout()
        horizontal_layout_3.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_3.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_3.addItem(spacerItem)
        
        self.button_create_macro_background = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_3.addWidget(self.button_create_macro_background)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_3.addItem(spacerItem)
        
        horizontal_layout_3.setStretch(0, 1)
        horizontal_layout_3.setStretch(1, 5)
        horizontal_layout_3.setStretch(2, 1)
        
        vertical_layout.addItem(horizontal_layout_3)
        
        return vertical_layout
    
    def setup_offset_title_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.label_offsets = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.label_offsets)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout

    def setup_offset_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        #item 0
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)
        grid_layout.setVerticalSpacing(0)
        
        self.label_10x_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_10x_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20x_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_20x_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50x_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_50x_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100x_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_100x_offset.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_X_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_X_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_Y_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z_offset = Title(self.central_widget,self.resolution_scaling)
        self.label_Z_offset.setAlignment(QtCore.Qt.AlignCenter)
        
        width = self.resolution_scaling.get_width_option_offset()
        self.line_edit_10x_X_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_10x_X_offset.setFixedWidth(width)
        self.line_edit_10x_X_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_10x_Y_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_10x_Y_offset.setFixedWidth(width)
        self.line_edit_10x_Y_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_10x_Z_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_10x_Z_offset.setFixedWidth(width)
        self.line_edit_10x_Z_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_20x_X_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_20x_X_offset.setFixedWidth(width)
        self.line_edit_20x_X_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_20x_Y_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_20x_Y_offset.setFixedWidth(width)
        self.line_edit_20x_Y_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_20x_Z_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_20x_Z_offset.setFixedWidth(width)
        self.line_edit_20x_Z_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_50x_X_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_50x_X_offset.setFixedWidth(width)
        self.line_edit_50x_X_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_50x_Y_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_50x_Y_offset.setFixedWidth(width)
        self.line_edit_50x_Y_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_50x_Z_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_50x_Z_offset.setFixedWidth(width)
        self.line_edit_50x_Z_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_100x_X_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_100x_X_offset.setFixedWidth(width)
        self.line_edit_100x_X_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_100x_Y_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_100x_Y_offset.setFixedWidth(width)
        self.line_edit_100x_Y_offset.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_100x_Z_offset = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_100x_Z_offset.setFixedWidth(width)
        self.line_edit_100x_Z_offset.setAlignment(QtCore.Qt.AlignRight)
        
        grid_layout.addWidget(self.label_X_offset, 0, 1, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.label_Y_offset, 0, 2, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.label_Z_offset, 0, 3, QtCore.Qt.AlignCenter)
        
        grid_layout.addWidget(self.label_10x_offset, 1, 0, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.label_20x_offset, 2, 0, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.label_50x_offset, 3, 0, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.label_100x_offset, 4, 0, QtCore.Qt.AlignCenter)
        
        grid_layout.addWidget(self.line_edit_10x_X_offset, 1, 1, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_10x_Y_offset, 1, 2, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_10x_Z_offset, 1, 3, QtCore.Qt.AlignCenter)
        
        grid_layout.addWidget(self.line_edit_20x_X_offset, 2, 1, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_20x_Y_offset, 2, 2, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_20x_Z_offset, 2, 3, QtCore.Qt.AlignCenter)
        
        grid_layout.addWidget(self.line_edit_50x_X_offset, 3, 1, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_50x_Y_offset, 3, 2, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_50x_Z_offset, 3, 3, QtCore.Qt.AlignCenter)
        
        grid_layout.addWidget(self.line_edit_100x_X_offset, 4, 1, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_100x_Y_offset, 4, 2, QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.line_edit_100x_Z_offset, 4, 3, QtCore.Qt.AlignCenter)
        
        horizontal_layout.addItem(grid_layout)
        
        #item 0
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def retranslate_right_window_ui(self, MainWindow):
        self.retranslate_left_pannel_ui(MainWindow)
        self.retranslate_right_pannel_ui(MainWindow)
        
    def retranslate_left_pannel_ui(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_widget_choose_calibration_ui(_translate)
        self.retranslate_widget_create_background_ui(_translate)
    
    def retranslate_right_pannel_ui(self,_translate):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_offset_title_widget_ui(_translate)
        self.retranslate_offset_widget_ui(_translate)
    
    def retranslate_widget_choose_calibration_ui(self,_translate):
        self.label_calibration.setText(_translate("MainWindow", "Calibration Folder"))
        self.button_browse_calibration_folder.setText(_translate("MainWindow", " Browse "))
        self.calibration_path_window.setText(_translate("MainWindow", "Path:"))

    def retranslate_widget_create_background_ui(self, _translate):
        self.label_create_background.setText(_translate("MainWindow", "Create Background Picture"))
        self.button_5x_background.setText(_translate("MainWindow", "  5x  "))
        self.button_10x_background.setText(_translate("MainWindow", " 10x "))
        self.button_20x_background.setText(_translate("MainWindow", " 20x "))
        self.button_50x_background.setText(_translate("MainWindow", " 50x "))
        self.button_100x_background.setText(_translate("MainWindow", " 100x "))
        self.label_wafer_type.setText(_translate("MainWindow", "Wafer Type"))
        self.button_wafer_type.setText(_translate("MainWindow", "  Select  "))
        self.button_create_macro_background.setText(_translate("MainWindow", "  Create Macro  "))
    
    def retranslate_offset_title_widget_ui(self, _translate):
        self.label_offsets.setText(_translate("MainWindow", u"Offsets values ( µm )"))
    
    def retranslate_offset_widget_ui(self, _translate):
        self.label_X_offset.setText(_translate("MainWindow", "      X      "))
        self.label_Y_offset.setText(_translate("MainWindow", "      Y      "))
        self.label_Z_offset.setText(_translate("MainWindow", "      Z      "))
        
        self.label_10x_offset.setText(_translate("MainWindow", "10x"))
        self.label_20x_offset.setText(_translate("MainWindow", "20x"))
        self.label_50x_offset.setText(_translate("MainWindow", "50x"))
        self.label_100x_offset.setText(_translate("MainWindow", "100x"))
        

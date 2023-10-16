# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Style.GUI_Object import Title, Informator, ObjectiveButton, MacroButton
from Tabs.Ui_Tab import Ui_Tab
from Popup_Windows.Load_Picture import Load_Picture

class Calibration_Tab(Ui_Tab):   
    def define_tab_number(self):
        return 3
        
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
        widget_open_or_new_calibration = self.setup_open_or_new_calibration()
        vertical_layout_main.addItem(widget_open_or_new_calibration)
        
       #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #item 2
        widget_nosepiece_calibration = self.setup_nosepiece_calibration()
        vertical_layout_main.addItem(widget_nosepiece_calibration)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #item 4
        widget_add_point = self.setup_add_point()
        vertical_layout_main.addItem(widget_add_point)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #item 4
        widget_add_point = self.setup_aspect_ratio()
        vertical_layout_main.addItem(widget_add_point)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        
        return vertical_layout_main
    
    def setup_right_pannel(self):
        vertical_layout_right = QtWidgets.QVBoxLayout()
        vertical_layout_right.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_right_pannel()
        vertical_layout_right.setSpacing(spacing)
        
        #item 1
        title = self.setup_information_title_widget()
        vertical_layout_right.addItem(title)
        
        #item 2
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 3
        info_label = self.setup_information_widget()
        vertical_layout_right.addItem(info_label)
        
        #item 4
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 5
        save_cancel = self.setup_save_cancel_calibration()
        vertical_layout_right.addItem(save_cancel)
        
        
        return vertical_layout_right
    
    def setup_open_or_new_calibration(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_open_or_new_calibration = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_open_or_new_calibration)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(spacing)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_create_new = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_create_new)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_open_existing = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_open_existing)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
        
    def setup_nosepiece_calibration(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_nosepiece = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_nosepiece)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_1.setSpacing(0)
        
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vhspacing_nosepiece_calibration()
        grid_layout.setSpacing(spacing)
        vspacing = self.resolution_scaling.get_vspacing_nosepiece_calibration()
        grid_layout.setVerticalSpacing(vspacing)
        
        self.button_5x_calibration = ObjectiveButton(self.central_widget,self.resolution_scaling)
        self.button_10x_calibration = ObjectiveButton(self.central_widget,self.resolution_scaling)
        self.button_20x_calibration = ObjectiveButton(self.central_widget,self.resolution_scaling)
        self.button_50x_calibration = ObjectiveButton(self.central_widget,self.resolution_scaling)
        self.button_100x_calibration = ObjectiveButton(self.central_widget,self.resolution_scaling)
        
        self.label_number_of_points = QtWidgets.QLabel(self.central_widget)
        
        self.label_5x_calibration = QtWidgets.QLabel(self.central_widget)
        self.label_5x_calibration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10x_calibration = QtWidgets.QLabel(self.central_widget)
        self.label_10x_calibration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20x_calibration = QtWidgets.QLabel(self.central_widget)
        self.label_20x_calibration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50x_calibration = QtWidgets.QLabel(self.central_widget)
        self.label_50x_calibration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100x_calibration = QtWidgets.QLabel(self.central_widget)
        self.label_100x_calibration.setAlignment(QtCore.Qt.AlignCenter)
        
        grid_layout.addWidget(self.button_5x_calibration, 0, 1)
        grid_layout.addWidget(self.button_10x_calibration, 0, 2)
        grid_layout.addWidget(self.button_20x_calibration, 0, 3)
        grid_layout.addWidget(self.button_50x_calibration, 0, 4)
        grid_layout.addWidget(self.button_100x_calibration, 0, 5)
        
        grid_layout.addWidget(self.label_number_of_points, 1, 0)
        
        grid_layout.addWidget(self.label_5x_calibration, 1, 1)
        grid_layout.addWidget(self.label_10x_calibration, 1, 2)
        grid_layout.addWidget(self.label_20x_calibration, 1, 3)
        grid_layout.addWidget(self.label_50x_calibration, 1, 4)
        grid_layout.addWidget(self.label_100x_calibration, 1, 5)
        
        horizontal_layout_1.addItem(grid_layout)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_add_point(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_add_point = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_add_point)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        
        self.button_load_picture = QtWidgets.QToolButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_load_picture)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_plot_calibration = QtWidgets.QToolButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_plot_calibration)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_aspect_ratio(self):
        
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_aspect_ratio()
        horizontal_layout.setSpacing(spacing)
        
        self.label_aspect_ratio = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.label_aspect_ratio)

        self.line_edit_aspect_ratio_min = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_gain_line_edit()
        self.line_edit_aspect_ratio_min.setFixedWidth(width)
        self.line_edit_aspect_ratio_min.setValidator(QtGui.QIntValidator(1, 100))
        self.line_edit_aspect_ratio_min.setAlignment(QtCore.Qt.AlignRight)
        horizontal_layout.addWidget(self.line_edit_aspect_ratio_min)
        
        self.label_to = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.label_to)
        
        self.line_edit_aspect_ratio_max = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_gain_line_edit()
        self.line_edit_aspect_ratio_max.setFixedWidth(width)
        self.line_edit_aspect_ratio_max.setValidator(QtGui.QIntValidator(1, 100))
        self.line_edit_aspect_ratio_max.setAlignment(QtCore.Qt.AlignRight)
        horizontal_layout.addWidget(self.line_edit_aspect_ratio_max)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def setup_information_title_widget(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.label_information = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.label_information)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def setup_information_widget(self):
        grid_spacing = self.resolution_scaling.get_gridspacing_calibration_information() #50
        thickness_spacing = self.resolution_scaling.get_spacing_thickness_information() #40
        width_thickness = self.resolution_scaling.get_width_thickness_information() #120
        
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(grid_spacing)
        
        self.label_calibration_name = QtWidgets.QLabel(self.central_widget)
        self.label_wafer_type = QtWidgets.QLabel(self.central_widget)
        self.label_oxide_type = QtWidgets.QLabel(self.central_widget)
        self.label_wafer_thickness = QtWidgets.QLabel(self.central_widget)
        self.label_oxide_thickness = QtWidgets.QLabel(self.central_widget)
        self.label_brand = QtWidgets.QLabel(self.central_widget)
        self.label_resistivity = QtWidgets.QLabel(self.central_widget)
        
        grid_layout.addWidget(self.label_calibration_name, 0, 0)
        grid_layout.addWidget(self.label_wafer_type, 1, 0)
        grid_layout.addWidget(self.label_oxide_type, 2, 0)
        grid_layout.addWidget(self.label_wafer_thickness, 3, 0)
        grid_layout.addWidget(self.label_oxide_thickness, 4, 0)
        grid_layout.addWidget(self.label_brand, 5, 0)
        grid_layout.addWidget(self.label_resistivity, 6, 0)
        
        self.line_edit_calibration_name = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_wafer_type = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_oxide_type = QtWidgets.QLineEdit(self.central_widget)
        
        horizontal_layout_wt = QtWidgets.QHBoxLayout()
        horizontal_layout_wt.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_wt.setSpacing(thickness_spacing)
        self.line_edit_wafer_thickness = QtWidgets.QLineEdit(self.central_widget)
        horizontal_layout_wt.addWidget(self.line_edit_wafer_thickness)
        self.label_wafer_thickness_unit = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_wt.addWidget(self.label_wafer_thickness_unit)
        
        self.line_edit_wafer_thickness.setFixedWidth(width_thickness)
        self.line_edit_wafer_thickness.setValidator(QtGui.QIntValidator(0, 99999))
        self.line_edit_wafer_thickness.setAlignment(QtCore.Qt.AlignRight)
        
        horizontal_layout_ot = QtWidgets.QHBoxLayout()
        horizontal_layout_ot.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_ot.setSpacing(thickness_spacing)
        self.line_edit_oxide_thickness = QtWidgets.QLineEdit(self.central_widget)
        horizontal_layout_ot.addWidget(self.line_edit_oxide_thickness)
        self.label_oxide_thickness_unit = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_ot.addWidget(self.label_oxide_thickness_unit)
        
        self.line_edit_oxide_thickness.setFixedWidth(width_thickness)
        self.line_edit_oxide_thickness.setValidator(QtGui.QIntValidator(0, 99999))
        self.line_edit_oxide_thickness.setAlignment(QtCore.Qt.AlignRight)
        
        self.line_edit_brand = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_resistivity = QtWidgets.QLineEdit(self.central_widget)
        
        grid_layout.addWidget(self.line_edit_calibration_name, 0, 1)
        grid_layout.addWidget(self.line_edit_wafer_type, 1, 1)
        grid_layout.addWidget(self.line_edit_oxide_type, 2, 1)
        grid_layout.addItem(horizontal_layout_wt, 3, 1)
        grid_layout.addItem(horizontal_layout_ot, 4, 1)
        grid_layout.addWidget(self.line_edit_brand, 5, 1)
        grid_layout.addWidget(self.line_edit_resistivity, 6, 1)
        
        horizontal_layout.addItem(grid_layout)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        horizontal_layout.setStretch(0, 10)
        horizontal_layout.setStretch(1, 100)
        horizontal_layout.setStretch(2, 10)
        
        return horizontal_layout
        
    
    def setup_save_cancel_calibration(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_save = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_save)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_cancel = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_cancel)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def load_picture(self):
        self.pop_up = Load_Picture(self.resolution_scaling)
        self.pop_up.show()
    
    def connect_buttons(self):
        self.button_load_picture.clicked.connect(self.load_picture)
    
    
    def retranslate_right_window_ui(self, MainWindow):
        self.retranslate_left_pannel_ui(MainWindow)
        self.retranslate_right_pannel_ui(MainWindow)
        
    def retranslate_left_pannel_ui(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_widget_open_or_new_calibration_ui(_translate)
        self.retranslate_widget_nosepiece_calibration_ui(_translate)
        self.retranslate_widget_add_point_ui(_translate)
        self.retranslate_widget_aspect_ratio_ui(_translate)
    
    def retranslate_right_pannel_ui(self,_translate):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_information_title_widget_ui(_translate)
        self.retranslate_information_widget_ui(_translate)
        self.retranslate_save_cancel_widget_ui(_translate)
    
    def retranslate_widget_open_or_new_calibration_ui(self,_translate):
        self.label_open_or_new_calibration.setText(_translate("MainWindow", "Calibration"))
        self.button_create_new.setText(_translate("MainWindow", " Open Existing "))
        self.button_open_existing.setText(_translate("MainWindow", " Create New "))

    def retranslate_widget_nosepiece_calibration_ui(self, _translate):
        self.label_nosepiece.setText(_translate("MainWindow", "Nosepiece to calibrate"))
        self.button_5x_calibration.setText(_translate("MainWindow", "  5x  "))
        self.button_10x_calibration.setText(_translate("MainWindow", " 10x "))
        self.button_20x_calibration.setText(_translate("MainWindow", " 20x "))
        self.button_50x_calibration.setText(_translate("MainWindow", " 50x "))
        self.button_100x_calibration.setText(_translate("MainWindow", " 100x "))
        self.label_number_of_points.setText(_translate("MainWindow", "Points    "))
        self.label_5x_calibration.setText(_translate("MainWindow", "  0  "))
        self.label_10x_calibration.setText(_translate("MainWindow", " 0 "))
        self.label_20x_calibration.setText(_translate("MainWindow", " 0 "))
        self.label_50x_calibration.setText(_translate("MainWindow", " 0 "))
        self.label_100x_calibration.setText(_translate("MainWindow", " 0 "))
    
    def retranslate_widget_add_point_ui(self, _translate):
        self.label_add_point.setText(_translate("MainWindow", "Add point"))
        self.button_load_picture.setText(_translate("MainWindow", "  Load Picture  "))
        self.button_plot_calibration.setText(_translate("MainWindow", "  Plot Calibration  "))
    
    def retranslate_widget_aspect_ratio_ui(self, _translate):
        self.label_aspect_ratio.setText(_translate("MainWindow", "Aspect Ratio  "))
        self.label_to.setText(_translate("MainWindow", "to"))
        self.line_edit_aspect_ratio_min.setText(_translate("MainWindow", "1"))
        self.line_edit_aspect_ratio_max.setText(_translate("MainWindow", "10"))
    
    def retranslate_information_title_widget_ui(self, _translate):
        self.label_information.setText(_translate("MainWindow", "Information"))
    
    def retranslate_information_widget_ui(self, _translate):
        self.label_calibration_name.setText(_translate("MainWindow", "Name"))
        self.label_wafer_type.setText(_translate("MainWindow", "Wafer"))
        self.label_oxide_type.setText(_translate("MainWindow", "Oxide"))
        self.label_wafer_thickness.setText(_translate("MainWindow", "Wafer thickness"))
        self.label_oxide_thickness.setText(_translate("MainWindow", "Oxide thickness"))
        self.label_brand.setText(_translate("MainWindow", "Brand"))
        self.label_resistivity.setText(_translate("MainWindow", "Resistivity"))
        
        # self.line_edit_calibration_name.setText(_translate("MainWindow", "Calibration Name"))
        # self.line_edit_wafer_type.setText(_translate("MainWindow", "Si"))
        # self.line_edit_oxide_type.setText(_translate("MainWindow", "SiO2"))
        # self.line_edit_wafer_thickness.setText(_translate("MainWindow", "700"))
        # self.line_edit_oxide_thickness.setText(_translate("MainWindow", "2850"))
        # self.line_edit_brand.setText(_translate("MainWindow", "Nova"))
        # self.line_edit_resistivity.setText(_translate("MainWindow", "low resist"))
        
        self.label_wafer_thickness_unit.setText(_translate("MainWindow", u"µm"))
        self.label_oxide_thickness_unit.setText(_translate("MainWindow", u"Å"))
        
    
    def retranslate_save_cancel_widget_ui(self, _translate):
        self.button_save.setText(_translate("MainWindow", "  Save  "))
        self.button_cancel.setText(_translate("MainWindow", "  Cancel  "))

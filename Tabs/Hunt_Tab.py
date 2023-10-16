# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Style.GUI_Object import Title, Informator, ToolButton
from Tabs.Ui_Tab import Ui_Tab

class Hunt_Tab(Ui_Tab):   
    def define_tab_number(self):
        return 1
        
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
        vertical_layout_main = QtWidgets.QVBoxLayout()
        vertical_layout_main.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_left_pannel()
        vertical_layout_main.setSpacing(spacing)
        
        #widget 0
        widget_working_folder = self.setup_working_folder()
        vertical_layout_main.addItem(widget_working_folder)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #widget 1
        widget_number_wafers = self.setup_calibration_to_use()
        vertical_layout_main.addItem(widget_number_wafers)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #widget 2
        widget_area_ai = self.setup_area_ai()
        vertical_layout_main.addItem(widget_area_ai)
        
        #line and spacers
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)

        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        #widget 3
        widget_use_ai = self.setup_use_ai()
        vertical_layout_main.addItem(widget_use_ai)
        
        #item 4
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_main.addItem(spacerItem)
        
        return vertical_layout_main
    
    def setup_right_pannel(self):
        vertical_layout_right = self.setup_hunt_widget()
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
        
        self.button_browse_folder = ToolButton(self.central_widget, self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_browse_folder)
        
        self.path_window = Informator(self.central_widget,self.resolution_scaling)
        w,h = self.resolution_scaling.get_path_window_size()
        self.path_window.setFixedSize(w, h)
        self.path_window.setWordWrap(True)
        self.path_window.setAlignment(QtCore.Qt.AlignTop)

        horizontal_layout_1.addWidget(self.path_window)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
        
    def setup_calibration_to_use(self):
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
        
        self.button_calibration = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_calibration)
        
        self.calibration_window = Informator(self.central_widget,self.resolution_scaling)
        w,h = self.resolution_scaling.get_calibration_window_size()
        self.calibration_window.setFixedSize(w, h)
        self.calibration_window.setAlignment(QtCore.Qt.AlignTop)

        horizontal_layout_1.addWidget(self.calibration_window)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_area_ai(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_area_title = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_area_title)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(spacing)
        
        self.label_minimum_size = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_minimum_size)
        
        self.line_edit_minimum_size = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_minimum_size.setValidator(QtGui.QIntValidator(0, 1e9))
        self.line_edit_minimum_size.setAlignment(QtCore.Qt.AlignRight)
        horizontal_layout_1.addWidget(self.line_edit_minimum_size)
        
        self.label_micrometer2 = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_micrometer2)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_use_ai(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_ai = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_ai)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(20)
        
        self.checkbox_use_ai = QtWidgets.QCheckBox(self.central_widget)
        horizontal_layout_1.addWidget(self.checkbox_use_ai)
 
        space = self.resolution_scaling.get_space_ai()
        spacerItem = QtWidgets.QSpacerItem(space, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)   
 
        self.line_edit_threshold = QtWidgets.QLineEdit(self.central_widget)
        width = self.resolution_scaling.get_width_thresold_line_edit()
        self.line_edit_threshold.setFixedWidth(width)
        self.line_edit_threshold.setAlignment(QtCore.Qt.AlignRight)
        self.line_edit_threshold.setValidator(QtGui.QIntValidator(0, 99))
        horizontal_layout_1.addWidget(self.line_edit_threshold)
        
        self.label_thresold = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_thresold)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_hunt_widget(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_right_pannel()
        vertical_layout.setSpacing(spacing)
        
        ###
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.label_hunt = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_hunt)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        ###
        self.view_stitched_images = QtWidgets.QGraphicsView(self.central_widget)
        vertical_layout.addWidget(self.view_stitched_images)
        
        ###
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.button_hunt = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_0.addWidget(self.button_hunt)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.button_select_flakes = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_0.addWidget(self.button_select_flakes)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        return vertical_layout
    
    def retranslate_right_window_ui(self, MainWindow):
        self.retranslate_left_pannel_ui(MainWindow)
        self.retranslate_right_pannel_ui(MainWindow)
        
    def retranslate_left_pannel_ui(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_widget_working_folder_ui(_translate)
        self.retranslate_widget_calibration_to_use_ui(_translate)
        self.retranslate_widget_area_ui(_translate)
        self.retranslate_widget_use_ai_ui(_translate)
    
    def retranslate_right_pannel_ui(self,_translate):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_hunt_widget_ui(_translate)
    
    def retranslate_widget_working_folder_ui(self,_translate):
        self.label_working_folder.setText(_translate("MainWindow", "Working Folder"))
        self.button_browse_folder.setText(_translate("MainWindow", "Browse"))
        self.set_label_path_working_folder()


    def retranslate_widget_calibration_to_use_ui(self, _translate):
        self.label_calibration.setText(_translate("MainWindow", "Chose Calibration"))
        self.button_calibration.setText(_translate("MainWindow", " Select "))
        self.calibration_window.setText(_translate("MainWindow", "Calibration: "))
    
    def retranslate_widget_area_ui(self, _translate):
        self.label_area_title.setText(_translate("MainWindow", "Flake Size"))
        self.label_minimum_size.setText(_translate("MainWindow", "Minimum area"))
        self.line_edit_minimum_size.setText(_translate("MainWindow", "400"))
        self.label_micrometer2.setText(_translate("MainWindow", u"µm²"))
    
    def retranslate_widget_use_ai_ui(self, _translate):
        self.label_ai.setText(_translate("MainWindow", "Artificial Intelligence"))
        self.checkbox_use_ai.setText(_translate("MainWindow", "Activate"))
        self.label_thresold.setText(_translate("MainWindow", "% Threshold"))
        self.line_edit_threshold.setText(_translate("MainWindow", "50"))
    
    def retranslate_hunt_widget_ui(self, _translate):
        self.label_hunt.setText(_translate("MainWindow", "Hunt for Flakes"))
        self.button_hunt.setText(_translate("MainWindow", "  Hunt  "))
        self.button_select_flakes.setText(_translate("MainWindow", " Select Flakes "))

    def connect_buttons(self):
        self.button_browse_folder.clicked.connect(self.browse_working_folder)
    
    def browse_working_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self.central_widget, 'Select Working Folder', '')
        if path != ('', ''):
            self.variables.set_working_folder(path)
            self.set_label_path_working_folder()
    
    def set_label_path_working_folder(self):
        _translate = QtCore.QCoreApplication.translate
        path = self.variables.get_working_folder()
        self.path_window.setText(_translate("MainWindow", "Path: "+ path))
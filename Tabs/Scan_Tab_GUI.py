# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from Style.GUI_Object import Title, Informator, ObjectiveButton, MacroButton, PushButton, DropDown, ToolButton
from Tabs.Ui_Tab import Ui_Tab

class Scan_Tab_GUI(Ui_Tab):
    def __init__(self, icon, variables):
        super(Scan_Tab_GUI, self).__init__(icon, variables)
 
    def define_tab_number(self):
        return 0
        
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
        
        #item 0
        widget_working_folder = self.setup_working_folder()
        vertical_layout_left.addItem(widget_working_folder)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #item line
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_left.addWidget(line)
        
        
        #item 4
        widget_nosepiece = self.setup_nosepiece()
        vertical_layout_left.addItem(widget_nosepiece)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #item line
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_left.addWidget(line)
        
        
        #item X
        widget_initialise_stage = self.setup_initialise_stage()
        vertical_layout_left.addItem(widget_initialise_stage)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #item line
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_left.addWidget(line)
        
        #item 6
        widget_scan_options = self.setup_scan_options()
        vertical_layout_left.addItem(widget_scan_options)
        
        #item 7
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #item 8
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_left.addWidget(line)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        #item 9
        widget_start_scanning = self.setup_start_scanning()
        vertical_layout_left.addItem(widget_start_scanning)
        
        #item 5
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_left.addItem(spacerItem)
        
        return vertical_layout_left
    
    def setup_right_pannel(self):
        vertical_layout_right = self.setup_stitch_widget()
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
        self.path_window.setAlignment(QtCore.Qt.AlignTop)
        self.path_window.setWordWrap(True)
        horizontal_layout_1.addWidget(self.path_window)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_nosepiece(self):
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
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_nosepiece()
        horizontal_layout_1.setSpacing(spacing)
        
        self.button_5x = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_5x)
        
        self.button_10x = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_10x)
        
        self.button_20x = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_20x)
        
        self.button_50x = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_50x)
        
        self.button_100x = ObjectiveButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_100x)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_initialise_stage(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_initialise_stage = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_initialise_stage)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        margin = self.resolution_scaling.get_small_left_margin()
        horizontal_layout_1.setContentsMargins(margin, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_nosepiece()
        horizontal_layout_1.setSpacing(spacing)
        
        self.label_wafer_type = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_wafer_type)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.dropdown_wafer_type = DropDown(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.dropdown_wafer_type)
        
        self.add_wafer_types()
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_initialise_stage = PushButton(self.central_widget,self.resolution_scaling)
        horizontal_layout_1.addWidget(self.button_initialise_stage)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_scan_options(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_scan_options()
        vertical_layout.setSpacing(spacing)
        
        self.label_scan_options = Title(self.central_widget,self.resolution_scaling)
        vertical_layout.addWidget(self.label_scan_options)
        
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_scan_options()
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_stage_area = PushButton(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.button_stage_area)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.color_correction_option_button = PushButton(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.color_correction_option_button)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.auto_hunt_button = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.auto_hunt_button)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout)
        
        return vertical_layout
    
    def setup_start_scanning(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        bottom_margin = self.resolution_scaling.get_minimum_vspacing_left_pannel()
        horizontal_layout.setContentsMargins(0, 0, 0, bottom_margin/2)
        
        horizontal_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_start_scanning = MacroButton(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.button_start_scanning)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_abort = MacroButton(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.button_abort)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        return horizontal_layout
    
    def setup_stitch_widget(self):
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
        
        self.label_stitched_images = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_stitched_images)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_1.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.view_stitched_images = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.view_stitched_images)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        self.display_stage_or_ID() 
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        
        ###
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.button_stitch = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_0.addWidget(self.button_stitch)
        
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
        self.retranslate_widget_nosepiece_ui(_translate)
        self.retranslate_widget_initialise_stage_ui(_translate)
        self.retranslate_widget_scan_options_ui(_translate)
        self.retranslate_widget_start_scanning_ui(_translate)
    
    def retranslate_right_pannel_ui(self,_translate):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_stitch_image_widget_ui(_translate)
        
    
    def retranslate_widget_working_folder_ui(self,_translate):
        self.label_working_folder.setText(_translate("MainWindow", "Working Folder"))
        self.button_browse_folder.setText(_translate("MainWindow", "Browse"))
        self.set_label_path_working_folder()
    
    def retranslate_widget_nosepiece_ui(self, _translate):
        self.label_nosepiece.setText(_translate("MainWindow", "Nosepiece"))
        self.button_5x.setText(_translate("MainWindow", "  5x  "))
        self.switch_to_5x()
        self.button_10x.setText(_translate("MainWindow", " 10x "))
        self.button_20x.setText(_translate("MainWindow", " 20x "))
        self.button_50x.setText(_translate("MainWindow", " 50x "))
        self.button_100x.setText(_translate("MainWindow", " 100x "))
    
    def retranslate_widget_initialise_stage_ui(self, _translate):
        self.label_initialise_stage.setText(_translate("MainWindow", "Initialise Stage"))
        self.label_wafer_type.setText(_translate("MainWindow", "Wafer Type"))
        self.button_initialise_stage.setText(_translate("MainWindow", "Initialise"))
    
    def retranslate_widget_scan_options_ui(self, _translate):
        self.label_scan_options.setText(_translate("MainWindow", "Scanning Options"))
        self.button_stage_area.setText(_translate("MainWindow", "Stage Area"))
        self.color_correction_option_button.setText(_translate("MainWindow", " Color Correction "))
        self.auto_hunt_button.setText(_translate("MainWindow", "Auto Hunt"))

    def retranslate_widget_start_scanning_ui(self, _translate):
        self.button_start_scanning.setText(_translate("MainWindow", " Start Scanning "))
        self.button_abort.setText(_translate("MainWindow", " Abort "))
    
    def retranslate_stitch_image_widget_ui(self, _translate):
        self.label_stitched_images.setText(_translate("MainWindow", "Stage and Wafers"))
        self.button_stitch.setText(_translate("MainWindow", "  Force Stitch  "))
    
    def connect_buttons(self):
        self.button_browse_folder.clicked.connect(self.browse_working_folder)
        self.button_stage_area.clicked.connect(self.set_stage_area_option)
        self.button_initialise_stage.clicked.connect(self.initialise_stage)
        
        self.button_5x.clicked.connect(self.switch_to_5x)
        self.button_10x.clicked.connect(self.switch_to_10x)
        self.button_20x.clicked.connect(self.switch_to_20x)
        self.button_50x.clicked.connect(self.switch_to_50x)
        self.button_100x.clicked.connect(self.switch_to_100x)
        
        self.button_start_scanning.clicked.connect(self.start_scanning)
        self.button_abort.clicked.connect(self.abort)
    
    def display_stage_or_ID(self):
        if self.variables.has_ID:
            self.display_stage_ID_thread()
            return 0
        self.display_stage_thread()
        
    
    def switch_to_5x(self):
        self.button_5x.active_state()
        self.button_10x.passive_state()
        self.button_20x.passive_state()
        self.button_50x.passive_state()
        self.button_100x.passive_state()
        self.variables.set_nosepiece("5x")
        
    def switch_to_10x(self):
        self.button_5x.passive_state()
        self.button_10x.active_state()
        self.button_20x.passive_state()
        self.button_50x.passive_state()
        self.button_100x.passive_state()
        self.variables.set_nosepiece("10x")
        
    def switch_to_20x(self):
        self.button_5x.passive_state()
        self.button_10x.passive_state()
        self.button_20x.active_state()
        self.button_50x.passive_state()
        self.button_100x.passive_state()
        self.variables.set_nosepiece("20x")
    
    def switch_to_50x(self):
        self.button_5x.passive_state()
        self.button_10x.passive_state()
        self.button_20x.passive_state()
        self.button_50x.active_state()
        self.button_100x.passive_state()
        self.variables.set_nosepiece("50x")
    
    def switch_to_100x(self):
        self.button_5x.passive_state()
        self.button_10x.passive_state()
        self.button_20x.passive_state()
        self.button_50x.passive_state()
        self.button_100x.active_state()
        self.variables.set_nosepiece("100x")
    
    def add_wafer_types(self):
        pass

    def browse_working_folder(self):
        pass
    
    def initialise_stage(self):
        pass
    
    def set_stage_area_option(self):
        pass
    
    def display_stage_thread(self):
        pass
    
    def start_scanning(self):
        pass
        
    def abort(self):
        pass
            
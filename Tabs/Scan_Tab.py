# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap

from Popup_Windows.Window_Stage_Area import Window_Stage_Area
from Popup_Windows.Window_Initialise_Stage import Window_Initialise_Stage
from Backend import Backend
import os


from Tabs.Scan_Tab_GUI import Scan_Tab_GUI

class Scan_Tab(Scan_Tab_GUI):
    def __init__(self, icon, variables):
        super(Scan_Tab, self).__init__(icon, variables)
        
    def add_wafer_types(self):
        self.dropdown_wafer_type.addItem('285nm 700µm')
        self.dropdown_wafer_type.addItem('90nm 525µm')

    def browse_working_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self.central_widget, 'Select Working Folder', '')
        
        if path != ('', ''):
            self.variables.set_working_folder(path)
            self.set_label_path_working_folder()
            self.button_browse_folder.normal_state()
            
            self.variables.default_variables()
            self.display_stage_thread()
            
        if os.path.exists(path+"/wafers_position.jpg"):
            self.variables.has_quickscan = True
            self.load_mat_from_pic()
        
        if os.path.exists(path+"/wafers_position_id.jpg"):
            self.variables.has_ID = True
            self.load_ID_from_pic()

    def initialise_stage(self):
        self.button_initialise_stage.normal_state()
        self.pop_up = Window_Initialise_Stage(self.resolution_scaling, self.variables)
        self.pop_up.show()
    
    def set_label_path_working_folder(self):
        _translate = QCoreApplication.translate
        path = self.variables.get_working_folder()
        self.path_window.setText(_translate("MainWindow", "Path: "+ path))
    
    def store_number_wafers(self):
        number_wafers = int(self.line_edit_number_wafer.text())
        self.variables.set_number_wafers(number_wafers)
    
    def set_stage_area_option(self):
        self.button_stage_area.normal_state()
        self.pop_up = Window_Stage_Area(self.resolution_scaling, self.variables)
        self.pop_up.show()
    
    def load_mat_from_pic(self):
        self.thread_load_mat_from_pic = Backend.LoadMatrice(self.variables)
        self.thread_load_mat_from_pic.start()
        self.thread_load_mat_from_pic.signal_end.connect(self.display_stage_thread)
    
    def load_ID_from_pic(self):
        self.thread_load_ID_from_pic = Backend.LoadMatriceID(self.variables)
        self.thread_load_ID_from_pic.start()
        self.thread_load_ID_from_pic.signal_end.connect(self.display_stage_ID_thread)
    
    def display_stage_thread(self):
        self.thread_display_stage = Backend.DisplayStage(self.variables, self.resolution_scaling)
        self.thread_display_stage.start()
        self.thread_display_stage.signal_end.connect(self.display_stage)
    
    def display_stage_ID_thread(self):
        self.thread_display_stage_ID = Backend.DisplayStageID(self.variables, self.resolution_scaling)
        self.thread_display_stage_ID.start()
        self.thread_display_stage_ID.signal_end.connect(self.display_stage)
    
    def display_stage(self, image):
        self.view_stitched_images.setPixmap(QPixmap.fromImage(image))
    
    def display_ID_start_slowscan(self):
        self.thread_display_stage_ID = Backend.DisplayStageID(self.variables, self.resolution_scaling)
        self.thread_display_stage_ID.start()
        self.thread_display_stage_ID.signal_end.connect(self.display_stage_start_slowscan)
    
    def display_stage_start_slowscan(self, image):
        self.view_stitched_images.setPixmap(QPixmap.fromImage(image))
        self.thread_slowscan = Backend.SlowScan(self.variables)
    
    def start_scanning(self):
        startscan = True
        
        if self.variables.get_working_folder() == "":
            self.button_browse_folder.error_state()
            startscan = False
            
        if self.variables.is_stage_initialised() == False:
            self.button_initialise_stage.error_state()
            startscan = False
            
        if startscan:
            self.thread_quickscan = Backend.QuickScan(self.resolution_scaling, self.backend)
            self.thread_quickscan.start()
            self.thread_quickscan.signal_update_stage.connect(self.display_stage_thread)
            self.thread_quickscan.signal_end.connect(self.display_stage_ID_thread)
            self.thread_quickscan.signal_end.connect(self.display_ID_start_slowscan)
        
    def abort(self):
        if hasattr(self, "thread_quickscan") and self.thread_quickscan.isRunning():
            self.thread_quickscan.kill()
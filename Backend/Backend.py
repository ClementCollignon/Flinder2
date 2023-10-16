# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage

from Backend.Threads.Thread_QuickScan import Thread_QuickScan, Thread_Identify_Wafers,Thread_Prepare_SlowScan
from Backend.Threads.Thread_Convert_Image import Thread_Convert_Image
from Backend.Threads import Thread_SlowScan

import cv2

class QuickScan(QThread):
    signal_update_stage = pyqtSignal()
    signal_end = pyqtSignal()
    
    def __init__(self, variables):
        super(QuickScan, self).__init__(variables)
    
    def run(self):
        self.quick_scan()
    
    def quick_scan(self):
        self.thread_scan = Thread_QuickScan(self.variables)
        self.thread_scan.start()
        self.thread_scan.signal_update_stage.connect(self.update_stage)
        self.thread_scan.signal_quickscan_end.connect(self.identify_wafers)
    
    def identify_wafers(self):
        self.thread_identify = Thread_Identify_Wafers(self.variables)
        self.thread_identify.start()
        self.thread_identify.signal_idwafers_end.connect(self.prepare_slow_scan)
    
    def prepare_slow_scan(self):
        self.thread_prepare_slow_scan = Thread_Prepare_SlowScan(self.variables)
        self.thread_prepare_slow_scan.start()
        self.thread_prepare_slow_scan.signal_end.connect(self.end_of_thread)
    
    @pyqtSlot()
    def update_stage(self):
        self.signal_update_stage.emit()
    
    @pyqtSlot()
    def end_of_thread(self):
        self.signal_end.emit()
    
    def kill(self):
        if hasattr(self, "thread_scan") and self.thread_scan.isRunning():
            self.thread_scan.kill()

class SlowScan(QThread):
    signal_endscan = pyqtSignal()
    signal_endwafer = pyqtSignal()
    
    
    def __init__(self, variables):
        super(SlowScan, self).__init__(variables)
    
    def run(self):
        self.focus_and_scan()
        self.colorcorrect_stitch_hunt()
    
    def focus_and_scan(self):
        self.thread_focus_scan = Thread_SlowScan.Thread_SlowScan(self.variables)
        self.thread_focus_scan.start()
        self.thread_focus_scan.signal_endscan.connect(self.end_scan)
    
    def end_scan(self):
        pass
    
    def colorcorrect_stitch_hunt(self):
        self.thread_colorcorrect_stitch_hunt = 0
    
    def kill(self):
        if hasattr(self, "thread_focus_scan") and self.thread_focus_scan.isRunning():
            self.thread_focus_scan.kill()
        if hasattr(self, "thread_colorcorrect_stitch_hunt") and self.thread_colorcorrect_stitch_hunt.isRunning():
            self.thread_colorcorrect_stitch_hunt.kill()

class DisplayStage(QThread):
    signal_end = pyqtSignal(QImage)
    
    def __init__(self, variables, resolution_scaling):
        super(DisplayStage, self).__init__()
        self.variables = variables
        self.resolution_scaling = resolution_scaling

    def run(self):
        matrice = self.get_matrice()
        size = self.resolution_scaling.get_stage_matrice_size()
        self.convert_matrice(matrice, size)
    
    def get_matrice(self):
        return self.variables.get_mat_stage()
    
    def convert_matrice(self, matrice, size):
        self.thread_convert = Thread_Convert_Image((size,size), matrice)
        self.thread_convert.start()
        self.thread_convert.signal_QImage.connect(self.send_QImage)
    
    @pyqtSlot(QImage)
    def send_QImage(self, image):
        self.signal_end.emit(image)

class DisplayStageID(DisplayStage):
    signal_end = pyqtSignal(QImage)
    def __init__(self, variables, resolution_scaling):
        super(DisplayStageID, self).__init__(variables, resolution_scaling)
    
    def get_matrice(self):
        return self.variables.get_mat_stage_id()
    
class LoadMatrice(QThread):
    signal_end = pyqtSignal()
    
    def __init__(self, variables):
        super(LoadMatrice, self).__init__()
        self.variables = variables

    def run(self):
        mat = self.get_matrice()
        self.set_matrice(mat)
        self.signal_end.emit()
    
    def set_matrice(self, mat):
        self.variables.set_mat_stage(0,0,mat)
    
    def get_matrice(self):
        path = self.variables.get_working_folder()
        mat = cv2.imread(f"{path}/wafers_position.jpg")
        mat = cv2.cvtColor(mat, cv2.COLOR_RGB2GRAY)
        return mat

class LoadMatriceID(LoadMatrice):
    signal_end = pyqtSignal()
    
    def __init__(self, variables):
        super(LoadMatriceID, self).__init__(variables)
    
    def set_matrice(self, mat):
        self.variables.set_mat_stage_id(mat)
    
    def get_matrice(self):
        path = self.variables.get_working_folder()
        mat = cv2.imread(f"{path}/wafers_position_id.jpg")
        return mat
        # mat = cv2.cvtColor(mat, cv2.COLOR_RGB2GRAY)




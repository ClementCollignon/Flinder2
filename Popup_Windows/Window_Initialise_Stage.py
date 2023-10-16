# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from Style.GUI_Object import SmallButton
from PyQt5.QtCore import pyqtSlot, QTimer

from Backend.Threads.Thread_Microscope import Thread_Cam, Thread_Wait_Stage, Thread_Exposure_1
from Backend.Threads.Thread_Microscope import Thread_Stage_GoTo, Thread_Autofocus, Thread_Fast_Bkg

class Window_Initialise_Stage(QtWidgets.QMainWindow):
    def __init__(self, resolution_scaling, variables):
        super(Window_Initialise_Stage, self).__init__()
        self.variables = variables
        self.setObjectName("PopWindow")
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        
        self.resolution_scaling = resolution_scaling
        
        self.thread_cam = Thread_Cam(self.resolution_scaling, self.variables.my_scope)
        self.thread_cam.start()
        
        self.thread_wait_stage = Thread_Wait_Stage(self.variables.my_scope)
        self.thread_wait_stage.start()
        
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
        
        messages = self.setup_messages()
        self.horizontal_layout_master.addItem(messages)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_master.addItem(spacerItem)
        
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_layout_master.addWidget(line)
        
        video_feed = self.setup_videofeed()
        self.horizontal_layout_master.addItem(video_feed)
        
        self.setCentralWidget(self.central_widget)
        
        self.retranslate_popup()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def setup_messages(self):
        vertical_layout_0 = QtWidgets.QVBoxLayout()
        vertical_layout_0.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_spacing_popup_initialise_stage()
        vertical_layout_0.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_stage = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_0.addWidget(self.label_stage)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_1.setSpacing(0)
        
        self.label_auto_exposure1 = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_1.addWidget(self.label_auto_exposure1)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        horizontal_layout_2 = QtWidgets.QHBoxLayout()
        horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_2.setSpacing(0)
        
        self.label_manual_focus = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_2.addWidget(self.label_manual_focus)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_2.addItem(spacerItem)
        
        self.button_manual_focus = SmallButton(self.central_widget, self.resolution_scaling)
        horizontal_layout_2.addWidget(self.button_manual_focus)
        self.button_manual_focus.hide()
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_2.addItem(spacerItem)
        
        horizontal_layout_3 = QtWidgets.QHBoxLayout()
        horizontal_layout_3.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_3.setSpacing(0)
        
        self.label_focus_routine = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_3.addWidget(self.label_focus_routine)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_3.addItem(spacerItem)
        
        horizontal_layout_4 = QtWidgets.QHBoxLayout()
        horizontal_layout_4.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_4.setSpacing(0)
        
        self.label_auto_exposure2 = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_4.addWidget(self.label_auto_exposure2)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_4.addItem(spacerItem)
        
        horizontal_layout_5 = QtWidgets.QHBoxLayout()
        horizontal_layout_5.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_5.setSpacing(0)
        
        self.label_bkg_routine = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_5.addWidget(self.label_bkg_routine)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_5.addItem(spacerItem)
        
        
        vertical_layout_0.addItem(horizontal_layout_0)
        vertical_layout_0.addItem(horizontal_layout_1)
        vertical_layout_0.addItem(horizontal_layout_2)
        vertical_layout_0.addItem(horizontal_layout_3)
        vertical_layout_0.addItem(horizontal_layout_4)
        vertical_layout_0.addItem(horizontal_layout_5)

        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_0.addItem(spacerItem)
        
        return vertical_layout_0
    
    def setup_videofeed(self):
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.label_video_feed = QtWidgets.QLabel(self.central_widget)
        horizontal_layout_0.addWidget(self.label_video_feed)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        return horizontal_layout_0
    
    def exposure_routine1(self):
        _translate = QtCore.QCoreApplication.translate
        self.thread_exposure_routine1 = Thread_Exposure_1(self.variables.my_scope)
        self.thread_exposure_routine1.start()
        self.thread_exposure_routine1.exposureDone.connect(self.exposure1_done)
        
        self.label_auto_exposure1.setText(_translate("PopWindow", "• Tuning exposure & white balance"))
    
    def exposure_routine2(self):
        _translate = QtCore.QCoreApplication.translate
        self.thread_exposure_routine1 = Thread_Exposure_1(self.variables.my_scope)
        self.thread_exposure_routine1.start()
        self.thread_exposure_routine1.exposureDone.connect(self.exposure2_done)
        
        self.label_auto_exposure2.setText(_translate("PopWindow", "• Tuning exposure & white balance"))
    
    def go_to_ref(self):
        posX,posY=-5341,-4738
        self.goto_thread = Thread_Stage_GoTo(self.variables.my_scope,posX,posY)
        self.goto_thread.start()
        self.goto_thread.stageArrivedRef.connect(self.manual_focus)
    
    def focus_routine(self):
        #implement
        self.button_manual_focus.hide()
        _translate = QtCore.QCoreApplication.translate
        self.label_focus_routine.setText(_translate("PopWindow", "• Auto-focusing"))
        
        self.thread_autofocus = Thread_Autofocus(self.variables.my_scope)
        self.thread_autofocus.start()
        self.thread_autofocus.autofocusDone.connect(self.exposure_routine2)
        
    def background_correction_routine(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_bkg_routine.setText(_translate("PopWindow", "• Background correction routine"))
        
        self.thread_bkg_routine = Thread_Fast_Bkg(self.variables.my_scope, self.variables)
        self.thread_bkg_routine.start()
        self.thread_bkg_routine.fastBkgDone.connect(self.fast_bkg_done)
    
    def closeEvent(self, event):
        self.thread_cam.kill()
        self.thread_cam.quit()
        self.thread_wait_stage.quit()
        event.accept()
    
    def close_perso(self):
        self.thread_cam.kill()
        self.thread_cam.quit()
        self.thread_wait_stage.quit()
        self.thread_autofocus.quit()
        self.thread_bkg_routine.quit()
        self.thread_exposure_routine1.quit()
        self.close()
    
    @pyqtSlot()
    def fast_bkg_done(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_bkg_routine.setText(_translate("PopWindow", "• Background correction routine done"))
        self.timer=QTimer()
        self.timer.timeout.connect(self.close_perso)
        self.variables.initialise_stage()
        self.timer.start(1000)
    
    @pyqtSlot()
    def manual_focus(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_manual_focus.setText(_translate("PopWindow", "• Please do a rough \n  manual focus"))
        self.button_manual_focus.setText(_translate("PopWindow", " Done "))
        self.button_manual_focus.show()
        self.button_manual_focus.clicked.connect(self.focus_routine)
    
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label_video_feed.setPixmap(QPixmap.fromImage(image))
    
    @pyqtSlot()
    def stage_arrived(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_stage.setText(_translate("PopWindow", "• Stage at reference point"))
        self.exposure_routine1()
    
    @pyqtSlot()
    def exposure1_done(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_auto_exposure1.setText(_translate("PopWindow", "• Exposure & white balance done"))
        self.go_to_ref()
    
    @pyqtSlot()
    def exposure2_done(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_auto_exposure2.setText(_translate("PopWindow", "• Exposure & white balance done"))
        self.background_correction_routine()
    
    def connect_buttons(self):
        self.thread_cam.changePixmap.connect(self.setImage)
        self.thread_wait_stage.stageArrived.connect(self.stage_arrived)
    
        # self.button_reset.clicked.connect(self.reset)
        # self.button_validate.clicked.connect(self.routine_selector)
        
        # self.checkbox_use_autofocus.clicked.connect(self.switch_to_autofocus)
        # self.checkbox_use_zmap.clicked.connect(self.switch_to_zmap)
    
    def retranslate_popup(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PopWindow", "Initialise Stage"))
        self.label_stage.setText(_translate("PopWindow", "• Waiting for stage"))
        #self.label_do_focus.setText(_translate("PopWindow", " Roughly focus the stage "))
    
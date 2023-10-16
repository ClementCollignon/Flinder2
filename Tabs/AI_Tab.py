# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Style.GUI_Object import Title, Informator, ObjectiveButton, MacroButton
from Tabs.Ui_Tab import Ui_Tab

class AI_Tab(Ui_Tab):   
    def define_tab_number(self):
        return 4
        
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
        widget_open_or_new_calibration = self.setup_choose_calibration()
        vertical_layout_main.addItem(widget_open_or_new_calibration)
        
        #line and spacers
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)
        
        #item 1
        widget_check_database = self.setup_check_database()
        vertical_layout_main.addItem(widget_check_database)
        
        #line and spacers
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vertical_layout_main.addWidget(line)
        
        #item 2
        widget_train = self.setup_train()
        vertical_layout_main.addItem(widget_train)
        
        return vertical_layout_main
    
    def setup_right_pannel(self):
        vertical_layout_right = QtWidgets.QVBoxLayout()
        vertical_layout_right.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_minimum_vspacing_right_pannel()
        vertical_layout_right.setSpacing(spacing)
        
        #item 0
        title = self.setup_information_title_widget()
        vertical_layout_right.addItem(title)
        
        #item 1
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        #item 2
        info_label = self.setup_information_widget()
        vertical_layout_right.addItem(info_label)
        
        #item 3
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_right.addItem(spacerItem)
        
        vertical_layout_right.setStretch(0, 1)
        vertical_layout_right.setStretch(1, 1)
        vertical_layout_right.setStretch(2, 200)
        vertical_layout_right.setStretch(3, 80)
        
        return vertical_layout_right
    
    def setup_choose_calibration(self):
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
        
        self.button_browse_calibration = QtWidgets.QToolButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_browse_calibration)
        
        self.calibration_window = Informator(self.central_widget,self.resolution_scaling)
        w,h = self.resolution_scaling.get_calibration_window_size()
        self.calibration_window.setFixedSize(w, h)
        self.calibration_window.setAlignment(QtCore.Qt.AlignTop)

        horizontal_layout_1.addWidget(self.calibration_window)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        return vertical_layout
    
    def setup_check_database(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        self.label_database = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout.addWidget(self.label_database)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        self.button_clean_database = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout.addWidget(self.button_clean_database)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        horizontal_layout.setStretch(0, 0)
        horizontal_layout.setStretch(1, 10)
        horizontal_layout.setStretch(2, 0)
        horizontal_layout.setStretch(3, 50)
        
        return horizontal_layout
    
    def setup_train(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_working_folder()
        vertical_layout.setSpacing(spacing)
        
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        self.label_train = Title(self.central_widget,self.resolution_scaling)
        horizontal_layout_0.addWidget(self.label_train)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_0)
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_hspacing_working_folder()
        horizontal_layout_1.setSpacing(spacing)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        self.button_initialize = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_initialize)
        
        self.button_train = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_train)
        
        self.button_save_CNN = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_1.addWidget(self.button_save_CNN)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        self.view_training = QtWidgets.QGraphicsView(self.central_widget)
        vertical_layout.addWidget(self.view_training)
        
        return vertical_layout
    
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
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        
        #item 0
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        #item 1
        labels = self.setup_labels_information_widget()
        horizontal_layout.addItem(labels)
        
        #item 2
        indicators = self.setup_indicator_information_widget()
        horizontal_layout.addItem(indicators)
        
        #item 3
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        
        horizontal_layout.setStretch(0, 25)
        horizontal_layout.setStretch(1, 50)
        horizontal_layout.setStretch(2, 50)
        horizontal_layout.setStretch(3, 25)
        
        return horizontal_layout

    def setup_labels_information_widget(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_information_AI()
        vertical_layout.setSpacing(spacing)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.label_good_ID = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_good_ID)
        vertical_layout.addItem(item)
        
        self.label_bad_ID = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_bad_ID)
        vertical_layout.addItem(item)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.label_last_save = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_last_save)
        vertical_layout.addItem(item)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.label_previous_loss = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_previous_loss)
        vertical_layout.addItem(item)
        
        self.label_previous_accuracy = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_previous_accuracy)
        vertical_layout.addItem(item)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.label_new_loss = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_new_loss)
        vertical_layout.addItem(item)
        
        self.label_new_accuracy = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_left_label_info_widget(self.label_new_accuracy)
        vertical_layout.addItem(item)
        
        return vertical_layout
    
    def setup_indicator_information_widget(self):
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        spacing = self.resolution_scaling.get_vspacing_information_AI()
        vertical_layout.setSpacing(spacing)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.indicator_good_ID = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_good_ID)
        vertical_layout.addItem(item)
        
        self.indicator_bad_ID = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_bad_ID)
        vertical_layout.addItem(item)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.indicator_last_save = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_last_save)
        vertical_layout.addItem(item)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.indicator_previous_loss = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_previous_loss)
        vertical_layout.addItem(item)
        
        self.indicator_previous_accuracy = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_previous_accuracy)
        vertical_layout.addItem(item)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        self.indicator_new_loss = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_new_loss)
        vertical_layout.addItem(item)
        
        self.indicator_new_accuracy = QtWidgets.QLabel(self.central_widget)
        item = self.create_flush_right_label_info_widget(self.indicator_new_accuracy)
        vertical_layout.addItem(item)
        
        return vertical_layout
    
    def create_flush_right_label_info_widget(self,label):   
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        horizontal_layout.addWidget(label)
        return horizontal_layout
    
    def create_flush_left_label_info_widget(self,label):   
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        horizontal_layout.addWidget(label)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacerItem)
        return horizontal_layout
    
    def retranslate_right_window_ui(self, MainWindow):
        self.retranslate_left_pannel_ui(MainWindow)
        self.retranslate_right_pannel_ui(MainWindow)
        
    def retranslate_left_pannel_ui(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_widget_choose_calibration_ui(_translate)
        self.retranslate_widget_check_database_ui(_translate)
        self.retranslate_widget_train_ui(_translate)
    
    def retranslate_right_pannel_ui(self,_translate):
        _translate = QtCore.QCoreApplication.translate
        self.retranslate_information_title_widget_ui(_translate)
        self.retranslate_information_widget_ui(_translate)
    
    def retranslate_widget_choose_calibration_ui(self,_translate):
        self.label_calibration.setText(_translate("MainWindow", "Select Calibration"))
        self.button_browse_calibration.setText(_translate("MainWindow", " Browse "))
        self.calibration_window.setText(_translate("MainWindow", "Name:"))

    def retranslate_widget_check_database_ui(self, _translate):
        self.label_database.setText(_translate("MainWindow", "Check Data Base"))
        self.button_clean_database.setText(_translate("MainWindow", " Clean "))
    
    def retranslate_widget_train_ui(self, _translate):
        self.label_train.setText(_translate("MainWindow", "Train AI"))
        self.button_initialize.setText(_translate("MainWindow", " Initialize "))
        self.button_train.setText(_translate("MainWindow", " Train "))
        self.button_save_CNN.setText(_translate("MainWindow", " Save "))
    
    def retranslate_information_title_widget_ui(self, _translate):
        self.label_information.setText(_translate("MainWindow", "Information"))
    
    def retranslate_information_widget_ui(self, _translate):
        self.label_good_ID.setText(_translate("MainWindow", "Good Flakes:"))
        self.label_bad_ID.setText(_translate("MainWindow", "Bad Flakes:"))
        self.label_last_save.setText(_translate("MainWindow", "Last Saved:"))
        self.label_previous_loss.setText(_translate("MainWindow", "Previous Loss:"))
        self.label_previous_accuracy.setText(_translate("MainWindow", "Previous Accuracy:"))
        self.label_new_loss.setText(_translate("MainWindow", "New Loss:"))
        self.label_new_accuracy.setText(_translate("MainWindow", "New Accuracy:"))
        
        self.indicator_good_ID.setText(_translate("MainWindow", "0"))
        self.indicator_bad_ID.setText(_translate("MainWindow", "0"))
        self.indicator_last_save.setText(_translate("MainWindow", "Never"))
        self.indicator_previous_loss.setText(_translate("MainWindow", "None"))
        self.indicator_previous_accuracy.setText(_translate("MainWindow", "None"))
        self.indicator_new_loss.setText(_translate("MainWindow", "None"))
        self.indicator_new_accuracy.setText(_translate("MainWindow", "None"))

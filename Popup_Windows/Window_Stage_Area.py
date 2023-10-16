# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Style.GUI_Object import Title

class Window_Stage_Area(QtWidgets.QMainWindow):
    def __init__(self, resolution_scaling, variables):
        super(Window_Stage_Area, self).__init__()
        
        self.setObjectName("PopWindow")
        self.setWindowIcon(QtGui.QIcon('Style/Icon.png'))
        
        self.resolution_scaling = resolution_scaling
        self.variables = variables
        
        width,height = self.resolution_scaling.get_popup_stage_area_size()
        
        self.number_wafers = 1
        
        self.resize(width,height)
        
        self.setup_ui()
        self.connect_buttons()
        
        self.retranslate_popup()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    
    def setup_ui(self):        
        self.central_widget = QtWidgets.QWidget(self)
        
        self.vertical_layout_master = QtWidgets.QVBoxLayout(self.central_widget)
        margin = self.resolution_scaling.get_margin_popup()
        self.vertical_layout_master.setContentsMargins(margin, margin, margin, margin)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_master.addItem(spacerItem)
        
        picture = self.setup_picture()
        self.vertical_layout_master.addItem(picture)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_master.addItem(spacerItem)
        
        cancel_or_validate = self.setup_cancel_validate()
        self.vertical_layout_master.addItem(cancel_or_validate)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_master.addItem(spacerItem)
        
        self.setCentralWidget(self.central_widget)
        
        self.retranslate_popup()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def setup_cancel_validate(self):
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.button_cancel = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_0.addWidget(self.button_cancel)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        self.button_validate = QtWidgets.QPushButton(self.central_widget)
        horizontal_layout_0.addWidget(self.button_validate)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        horizontal_layout_0.setStretch(0, 100)
        horizontal_layout_0.setStretch(1, 100)
        horizontal_layout_0.setStretch(2, 50)
        horizontal_layout_0.setStretch(3, 100)
        horizontal_layout_0.setStretch(4, 100)
        
        return horizontal_layout_0
    
    def setup_picture(self):
        horizontal_layout_0 = QtWidgets.QHBoxLayout()
        horizontal_layout_0.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_0.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        pic_path = "Style/Icons/stage_size.png"
        
        vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        label = QtWidgets.QLabel(self.central_widget)
        pixmap = QtGui.QPixmap(pic_path)
        scale = self.resolution_scaling.get_size_popup_picture()
        pixmap=pixmap.scaled(QtCore.QSize(scale,scale), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        
        vertical_layout.addWidget(label)
        
        
        horizontal_layout_1 = QtWidgets.QHBoxLayout()
        horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_1.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        width = self.resolution_scaling.get_width_line_edit_stage_area()
        self.line_edit_W = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_W.setFixedWidth(width)
        self.line_edit_W.setAlignment(QtCore.Qt.AlignRight)
        self.line_edit_W.setValidator(QtGui.QIntValidator(10,100))
        
        self.label_W = QtWidgets.QLabel(self.central_widget)
        
        horizontal_layout_1.addWidget(self.line_edit_W)
        horizontal_layout_1.addWidget(self.label_W)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_1.addItem(spacerItem)
        
        vertical_layout.addItem(horizontal_layout_1)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addItem(spacerItem)
        
        horizontal_layout_0.addItem(vertical_layout)
        
        
        vertical_layout_1 = QtWidgets.QVBoxLayout(self.central_widget)
        vertical_layout_1.setContentsMargins(0, 0, 0, 0)
        vertical_layout_1.setSpacing(0)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_1.addItem(spacerItem)
        
        horizontal_layout_2 = QtWidgets.QHBoxLayout()
        horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        horizontal_layout_2.setSpacing(0)
        
        width = self.resolution_scaling.get_width_line_edit_stage_area()
        self.line_edit_H = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_H.setFixedWidth(width)
        self.line_edit_H.setAlignment(QtCore.Qt.AlignRight)
        self.line_edit_H.setValidator(QtGui.QIntValidator(10,75))
        
        self.label_H = QtWidgets.QLabel(self.central_widget)
        
        horizontal_layout_2.addWidget(self.line_edit_H)
        horizontal_layout_2.addWidget(self.label_H)
        
        vertical_layout_1.addItem(horizontal_layout_2)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vertical_layout_1.addItem(spacerItem)
        
        horizontal_layout_0.addItem(vertical_layout_1)
        
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout_0.addItem(spacerItem)
        
        return horizontal_layout_0
    
    def connect_buttons(self):
        self.button_cancel.clicked.connect(self.close)
        self.button_validate.clicked.connect(self.collect_values)
        
    def collect_values(self):
        H = self.line_edit_H.text()
        W = self.line_edit_W.text()
        
        self.variables.set_stage_area(int(H), int(W))
        
        self.close()
        
    
    def retranslate_popup(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PopWindow", "Stage Area"))
        self.button_cancel.setText(_translate("PopWindow", " Cancel "))
        self.button_validate.setText(_translate("PopWindow", " Validate "))
        
        self.label_W.setText(_translate("PopWindow", " mm"))
        self.label_H.setText(_translate("PopWindow", " mm"))
        
        self.retranslate_line_edit_from_stored_values(_translate)
            
    def retranslate_line_edit_from_stored_values(self, _translate):
        H,W = self.variables.get_stage_area()
        
        self.line_edit_H.setText( _translate("PopWindow", str(H)) )
        self.line_edit_W.setText( _translate("PopWindow", str(W)) )
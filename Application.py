from PyQt5 import QtWidgets, QtCore
import sys
import os
from MainWindow import MainWindow
from Style.GUI_Object import Sizes



def main():
    QtCore.QLocale().setDefault(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    scaling_resolution = Sizes()
    file = open(scaling_resolution.get_style_sheet(),'r')
    
    with file:
        qss = file.read()
        app.setStyleSheet(qss)
        
    
    app.setQuitOnLastWindowClosed(True)
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
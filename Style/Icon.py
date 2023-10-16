# -*- coding: utf-8 -*-

from PyQt5 import QtGui

class Icon(object):
    def __init__(self, folder):
        passive_icon_names = ["Scan", "Hunt", "Zoom", "Calibration", "TrainAi", "Options"]
        
        self.icons_passive = [QtGui.QIcon(folder+"/"+name+".png") for name in passive_icon_names]
        self.icons_active = [QtGui.QIcon(folder+"/"+name+"_active.png") for name in passive_icon_names]
        
        self.icons_tab = []
        for i in range(len(self.icons_passive)):
            self.icons_tab.append(self.icons(i))
        
    def icons(self,tab_number):
        icons_list = []
        for i in range(len(self.icons_passive)):
            if i == tab_number:
                icons_list.append(self.icons_active[i])
            else:
                icons_list.append(self.icons_passive[i])
        return icons_list                
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, SIGNAL
from numpy import round
import os
import time


class Threaded_Zmapper(QThread):
    def __init__(self,variables):
        QThread.__init__(self)
        self.variables = variables
        self.path_zmap_macro = self.get_path_zmap_macro()
        self.position_path_list = []
        self.picture_path_list = []
        
    def __del__(self):
        self.wait()
    
    def run(self):
        ###CREATE ZMAP FOLDER if it doesnt exist
        self.create_zmap_folders()
         
        ###CREATE ZMAP MACRO
        self.create_zmap_macro()
        
        ###CREATE LIST OF PATH TO CHECK
        self.update_position_path_list()
        
        ###CHECK FOR path in PATHS and send signals for progress
        self.check_progress()
        
        ###Store the Z map
        #X,Y,Z,sharpness_score
        
        ##Implement progress bar
        ##Emit Done when done
        ##

    def get_path_zmap_macro_file(self):
        path = self.variables.get_working_folder()
        path += "//Macro_files//macro_zmap.dat"
        return path
    
    def get_path_macro_folder(self):
        path = self.variables.get_working_folder()
        path += "//Macro_files"
        return path
    
    def get_path_zmap_files_folder(self):
        path = self.variables.get_working_folder()
        path += "//Zmap_files"
        return path
    
    def get_paths_zmap_files_wafer_folder(self):
        path_list=[]
        path_zmap_files_folder = self.get_path_zmap_files_folder()
        number_of_wafers = self.variables.get_number_wafers()
        for i in range(number_of_wafers):
            target_path = path_zmap_files_folder+"//Wafer_"+str(i).zfill(2)
            path_list.append(target_path)
        return path_list
    
    def get_path_zmap_position_picture(self,wafer_number,point_number):
        path_Zfiles = self.get_path_zmap_files_folder()
        wafer_name = "Wafer_"+str(wafer_number).zfill(2)
        file_name = "position_"+str(point_number)+".dat"
        
        path_position = path_Zfiles+"\\"+wafer_name+"\\"+file_name
        path_picture = path_Zfiles+"\\"+wafer_name
        
        return path_position, path_picture  

    
    def create_folder(self,path):
        if os.path.exists(path) == False:
            os.mkdir(path)
    
    def create_zmap_folders(self):
        path_working_folder = self.variables.get_working_folder()
        self.create_folder(path_working_folder)
        
        path_macro_folder = self.get_path_macro_folder()
        self.create_folder(path_macro_folder)
            
        path_zmap_files_folder = self.get_path_zmap_files_folder()
        self.create_folder(path_zmap_files_folder)
        
        paths_zmap_files_wafer_folder = self.get_paths_zmap_files_wafer_folder()
        for path in paths_zmap_files_wafer_folder:
            self.create_folder(path)
    
    def create_zmap_macro(self):
        macro_zmap=""
        N = self.variables.get_number_wafers()
        
        for wafer_number in range(N):
            macro_1wafer = self.create_zmap_macro_1wafer(wafer_number)
            macro_zmap += macro_1wafer
        
        path_zmap_macro_file = self.get_path_zmap_macro_file()
        with open(path_zmap_macro_file, "w") as file:
            file.write(macro_zmap)
    
    def create_zmap_macro_1wafer(self,wafer_number):
        x0,y0,width,height = self.variables.get_wafer_position_size(wafer_number)
        number_of_points,z_range,steps = self.variables.get_zmap_parameters()
        number_of_points = int(number_of_points)
        
        positions = self.build_position_array_zmap(x0,y0,width,height,number_of_points)
        
        true_range = 2.*z_range
        steps_size = true_range/steps
        steps_size = round(steps_size,6)
        macro_prefocus = self.create_macro_prefocus(x0,y0,true_range,steps_size)
        
        macro_focus = self.create_macro_points(wafer_number,positions,true_range,steps_size)
        
        macro = macro_prefocus+macro_focus
        return macro
    
    def create_macro_points(self,wafer_number,positions,true_range,steps_size):
        macro=""
        point_number=0
        for position in positions:
            macro+=self.create_macro_1point(wafer_number,point_number,position,true_range,steps_size)
            point_number+=1
        return macro
    
    def create_macro_1point(self,wafer_number,point_number,position,zrange,zstep):
        macro="""
StgSetupFocus(2,"""+str(zstep)+""",0);
StgSetupFocusEx("""+str(zrange)+""",10);
StgMoveXY("""+str(position[0]*1000)+""", """+str(position[1]*1000)+""", 0);
StgFocus();
ZoomFitToScreen();
"""
        path_position,path_picture = self.get_path_zmap_position_picture(wafer_number,point_number)
        
        macro+="SaveNext_Images(\""+path_picture+"\", 4, \"position_\", 0);"
        macro+="AutoCapture();"
        macro+="ImageExportAllAvailableInfo(1,\""+path_position+");"
        
        return macro
    
    def create_macro_prefocus(self,x0,y0,zrange,zstep):
        zrange0,zstep0,xymove = self.variables.get_corner_focus_parameters()
        macro="""CameraSet_ToggleAE(1,0);
CameraFormatSet(1, "3x8_Kaiser_Full_Area_2.5x_1/3");
StgMoveXY("""+str(x0*1000)+""", """+str(y0*1000)+""", 0);
StgSetupFocus(2,"""+str(zstep0)+""",0);
StgSetupFocusEx("""+str(zrange0)+""",10);
StgFocus();
StgMoveXY("""+str(-xymove)+""", """+str(-xymove)+""", 1);
Wait(1.00000);
CameraCmd_AutoWhite();
CameraCmd_AutoExposure();
CameraCmd_AutoWhite();
Wait(1.00000);
StgSetupFocus(2,"""+str(zstep)+""",0);
StgSetupFocusEx("""+str(zrange)+""",10);
StgSetupFocusOffset(0.00000);
StgFocus();
ZoomFitToScreen();
Wait(1.00000);
CameraCmd_AutoWhite();
CameraCmd_AutoExposure();
CameraCmd_AutoWhite();
Wait(1.00000);
StgMoveXY("""+str(xymove)+""", """+str(xymove)+""", 1);
Wait(1.00000);
StgFocus();"""
        return macro    

    def build_position_array_zmap(self,x0,y0,width,height,points):
        margin = 0.05
        
        jump_x = (1 - 2*margin) * width
        jump_y = (1 - 2*margin) * height
        
        xi = x0 + margin * width
        yi = y0 + margin * height
        
        positions = []
        for i in range(points):
            xi += i*jump_x
            for j in range(points):
                if i%2 == 0:
                    yi += j*jump_y
                else:
                    yi -= j*jump_y
                positions.append([xi,yi])
        
        return positions

    def update_position_path_list(self):
        Nwafer = self.variables.get_number_wafers()
        Npoints,zrange,Nsteps = self.variables.get_zmap_parameters()
        
        position_path_list,picture_path_list=[],[]
        for wafer_number in range(Nwafer):
            for point_number in range(Npoints):
                position_path, position_picture = self.get_path_zmap_position_picture(wafer_number,point_number)
                position_path_list.append(position_path)
                picture_path_list.append(position_picture+"/position_"+str(point_number)+".jpg")
        
        self.position_path_list = position_path_list
        self.picture_path_list = picture_path_list

    def check_progress(self):
        N_focus_points = len(self.position_path_list)
        self.total_progress = 3*N_focus_points
        self.progress = 0
        
        for i in range(N_focus_points):
            self.check_position(i)
            self.send_progress()
            
            self.check_picture(i)
            self.send_progress()
            
            sharpness_score = self.get_sharpness_score(self.picture_path_list[i])
            x, y, z = self.get_position(i)
            self.send_progress()
            
            self.update_position(x,y,z,sharpness_score)
                
        return 0
    
    def check_position(self,position_number):
        while os.path.exists(self.position_path_list[position_number]) == False:
            time.sleep(0.5)
        self.progress += 1
    
    def check_picture(self,picture_number):
        while os.path.exists(self.picture_path_list[picture_number]) == False:
            time.sleep(0.5)
        self.progress += 1
        
    def send_progress(self):
        progress_percent = int(round(self.progress/self.total_progress*100,0))
        self.emit(SIGNAL('zmap_progress(QString)'), str(progress_percent))
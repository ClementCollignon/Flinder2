# -*- coding: utf-8 -*-

import numpy as np
from Microscope.Microscope import Microscope

class Variables(object):
    def __init__(self):
        self.working_folder=""
       
        self.nosepiece = "5x"
        
        #default parameters: Npoints(side of square), Range(+-), Nsteps
        self.default_autofocus_parameters_dict = {"5x":[3,3.0,7], "10x":[3,2.0,7], "20x":[3,1.0,7], "50x":[3,1.0,7], "100x":[3,1.0,7]}
        self.default_zmap_parameters_dict = {"5x":[3,10.0,41], "10x":[3,10.0,41], "20x":[3,10.0,41], "50x":[3,10.0,41], "100x":[3,10.0,41]}
        
        self.default_autofocus_parameters = self.default_autofocus_parameters_dict[self.nosepiece]
        self.default_zmap_parameters = self.default_zmap_parameters_dict[self.nosepiece]
        
        self.autofocus_parameters = self.default_autofocus_parameters
        self.zmap_parameters = self.default_zmap_parameters
        
        self.fast_bkg = True
        
        self.stage_area = (75, 100)
        
        x,y = int(self.stage_area[1]/3.)+1, int(self.stage_area[0]/3.)+1
        
        self.step_size = 3000
        self.square_size = int(self.step_size / 10)
        self.mat_stage = np.zeros((y*self.square_size,x*self.square_size),dtype = np.uint8)
        self.mat_stage_xy = np.zeros((y*self.square_size,x*self.square_size,2),dtype = np.uint8)
        self.mat_stage_id = np.zeros((y*self.square_size,x*self.square_size, 3),dtype = np.uint8)
        
        self.stage_initialised = False
        
        self.my_scope = Microscope("C:\Program Files\Micro-Manager-2.0",
                                            "Nikon_Ri2.cfg",
                                            self.get_nosepiece())
        
        self.overlap = 5
        self.factors={"5x" : 1, "10x" : 2, "20x" : 4, "50x" : 10, "100x" : 20}
        
        self.field_of_view = [2.8429,1.8906]
        
        self.has_quickscan = False
        self.has_ID = False
        
        self.num_focus_points = 20
        
        self.focus_positions = {}
        self.scan_positions = {}
        self.wafers_contours = {}
        self.plane_parameters = {}
    
    def set_plane_parameters(self, parameters, wafer_number):
        self.plane_parameters[wafer_number] = parameters
    
    def get_plane_parameters(self, wafer_number):
        try :
            return self.plane_parameters[wafer_number]
        except:
            return 0
    
    def set_xy_scan_positions(self, wafer_number, position_list):
        self.scan_positions[wafer_number] = position_list
    
    def set_xy_focus_positions(self, wafer_number, focus_list):
        self.focus_positions[wafer_number] = focus_list
    
    def get_xy_focus_positions(self):
        return self.focus_positions
    
    def get_xy_scan_positions(self):
        return self.scan_positions
    
    def set_wafer_contour(self, wafer_number, contour):
        self.wafers_contours[wafer_number] = contour
    
    def get_wafers_contours(self, wafer_number):
        return self.wafers_contours
    
    def set_num_focus_points(self, N):
        self.num_focus_points = N
    
    def get_num_focus_points(self):
        return self.num_focus_points
    
    def get_overlap_percent(self):
        return self.overlap
    
    def set_overlap_percent(self, new_overlap_value):
        self.overlap = new_overlap_value
    
    def get_field_of_view(self):
        scaling = self.factors[self.nosepiece]
        return [self.field_of_view[0]/scaling, self.field_of_view[1]/scaling]
        
    def default_variables(self):
        x,y = int(self.stage_area[1]/3.)+1, int(self.stage_area[0]/3.)+1
        self.step_size = 3000
        self.square_size = int(self.step_size / 10)
        self.mat_stage = np.zeros((y*self.square_size,x*self.square_size),dtype = np.uint8)
        self.mat_stage_xy = np.zeros((y*self.square_size,x*self.square_size,2),dtype = np.uint8)
        self.mat_stage_id = np.zeros((y*self.square_size,x*self.square_size, 3),dtype = np.uint8)
        self.has_quickscan = False
        self.has_ID = False
        
        self.focus_positions = {}
        self.scan_positions = {}
        self.wafers_contours = {}
    
    def get_step_size(self):
        return self.step_size

    def set_step_size(self, new_step_size):
        self.step_size = new_step_size
        self.square_size = int(self.step_size / 10)
    
    def get_square_size(self):
        return self.square_size
    
    def set_mat_stage_id(self, new_mat):
        self.mat_stage_id = new_mat
    
    def get_mat_stage_id(self):
        return self.mat_stage_id
    
    def is_stage_initialised(self):
        return self.stage_initialised
    
    def initialise_stage(self):
        self.stage_initialised = True
    
    def get_mat_stage(self):
        return self.mat_stage
    
    def set_mat_stage(self, i_min, j_min, mat):
        self.mat_stage[i_min:i_min+len(mat),j_min:j_min+len(mat[0])] = mat
    
    def get_mat_stage_xy(self):
        return self.mat_stage_xy
    
    def set_mat_stage_xy(self, i_min, j_min, size, xy):
        self.mat_stage_xy[i_min:i_min+size,j_min:j_min+size] = xy
    
    def get_stage_area(self):
        return self.stage_area
    
    def set_stage_area(self, h, w):
        self.stage_area = h, w
    
    def get_corner_focus_parameters(self):
        return self.zrange_corner_dict[self.nosepiece], self.zstep_corner_dict[self.nosepiece],  self.xymove_corner_dict[self.nosepiece]
    
    def set_working_folder(self,working_folder_path):
        self.working_folder = working_folder_path
    
    def set_fast_bkg(self, bkg):
        self.fast_bkg = bkg
    
    def get_fast_bkg(self, bkg):
        return self.fast_bkg
    
    def get_working_folder(self):
        return self.working_folder
    
    def set_number_wafers(self,number_wafers):
        self.number_wafers = number_wafers
    
    def get_number_wafers(self):
        return self.number_wafers
    
    def set_wafer_position_size(self, wafer_position_size):
        self.wafer_position_size = wafer_position_size
    
    def get_wafer_position_size(self, wafer_number):
        return self.wafer_position_size[wafer_number]
    
    def get_wafer_position_size_length(self):
        return len(self.wafer_position_size)
    
    def set_findwafer_status(self, new_value):
        self.findwafer_status = new_value
    
    def get_findwafer_status(self):
        return self.findwafer_status
    
    def get_autofocus_parameters(self):
        return self.autofocus_parameters
    
    def set_autofocus_parameters(self,parameters):
        self.autofocus_parameters = parameters
    
    def get_zmap_parameters(self):
        return self.zmap_parameters
    
    def set_zmap_parameters(self,parameters):
        self.zmap_parameters = parameters
        
    def reset_focus_parameters(self):
        self.autofocus_parameters = self.default_autofocus_parameters_dict[self.nosepiece]
        self.zmap_parameters = self.default_zmap_parameters_dict[self.nosepiece]
        self.focus_status = 0
      
    def get_nosepiece(self):
        return self.nosepiece
    
    def set_nosepiece(self,nosepiece):
        self.nosepiece = nosepiece
        self.reset_focus_parameters()
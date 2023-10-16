from PyQt5 import QtWidgets
from win32api import GetSystemMetrics

class Sizes():
    def __init__(self):
        self.resolution_height = self.get_resolution_height()
        self.index_resolution = self.get_index_resolution()

    def get_icon_tab_size(self):
        ICON_SIZE_TAB_DICT = {0: 25 , 1: 50, 2 : 50, 3: 75, 4: 100}
        return ICON_SIZE_TAB_DICT[self.index_resolution]

    def get_index_resolution(self):
        TYPICAL_SCREEN_HEIGHT = [0,720,1080,1440,2160,10000]
        for i in range(len(TYPICAL_SCREEN_HEIGHT)):
            if self.resolution_height >= TYPICAL_SCREEN_HEIGHT[i]:
                index = i
        return index
    
    def get_hspacing_right_window(self):
        HSPACING_DICT = {0: 7, 1: 15, 2 : 15, 3: 22, 4: 30}
        return HSPACING_DICT[self.index_resolution]
        
    def get_informator_size(self):
        INFORMATOR_SIZE_DICT = {0: 8, 1: 15, 2 : 15, 3: 20, 4: 30}
        return str(INFORMATOR_SIZE_DICT[self.index_resolution])
    
    def get_margin_main_window(self):
        MARGIN_MAIN_WINDOW_DICT = {0: (10,10,10,10), 1: (20,20,20,20) ,2 : (20,20,20,20), 3: (30,30,30,30), 4: (40,40,40,40)}
        return MARGIN_MAIN_WINDOW_DICT[self.index_resolution]
        
    def get_resolution_height(self):
        return GetSystemMetrics(1)
    
    def get_style_sheet(self):
        STYLE_SHEET_DICT = {0:"lowres", 1:"720", 2:"1080", 3:"2K", 4:"4K"}
        return f"Style/FlinderStyleSheet_{STYLE_SHEET_DICT[self.index_resolution]}.qss"
    
    def get_window_size(self):
        WINDOW_SIZE_DICT = {0: (600, 300), 1: (1200, 600),2 : (1200, 600), 3: (1800, 900), 4: (2400, 1200)}
        return WINDOW_SIZE_DICT[self.index_resolution]
    
    def get_popup_position_size_size(self):
        DICT = {0: (450, 100), 1: (900, 200),2 : (900, 200), 3: (1350, 300), 4: (1800, 400)}
        return DICT[self.index_resolution]
    
    # def get_popup_focus_size(self):
    #     DICT = {0: (450, 100), 1: (900, 200),2 : (900, 200), 3: (1350, 300), 4: (1000, 1000)}
        # return DICT[self.index_resolution]
    
    def get_stage_matrice_size(self):
        DICT = {0: 225, 1: 450, 2 : 450, 3: 675, 4: 900}
        return DICT[self.index_resolution]
    
    def get_popup_initialise_stage_size(self):
        DICT = {0: (500, 250), 1: (1000, 500),2 : (1000,500), 3: (1500, 750), 4: (2000, 1000)}
        return DICT[self.index_resolution]
    
    def get_popup_stage_area_size(self):
        DICT = {0: (250, 200), 1: (500, 400),2 : (500, 400), 3: (750, 600), 4: (1000, 800)}
        return DICT[self.index_resolution]
        
    def get_popup_wafers_positions_size(self):
        DICT = {0: (450, 100), 1: (900, 200),2 : (900, 200), 3: (1350, 300), 4: (1350, 300)}
        return DICT[self.index_resolution]
    
    def get_margin_popup(self):
        DICT = {0: 5, 1: 10, 2 : 10, 3: 15, 4: 20}
        return DICT[self.index_resolution]
    
    def get_margin_popup_focus(self):
        DICT = {0: 15, 1: 30, 2 : 30, 3: 45, 4: 60}
        return DICT[self.index_resolution]
    
    def get_margin_popup_initialise_stage(self):
        DICT = {0: 2, 1: 5, 2 : 20, 3: 8, 4: 20}
        return DICT[self.index_resolution]
    
    def get_spacing_popup_initialise_stage(self):
        DICT = {0: 2, 1: 5, 2 : 20, 3: 8, 4: 30}
        return DICT[self.index_resolution]
    
    def get_display_size_cam(self):
        DICT = {0: 150, 1: 300, 2 : 600, 3: 450, 4: 600}
        return DICT[self.index_resolution]
    
    def get_spacing_popup_table(self):
        DICT = {0: 5, 1: 10, 2 : 10, 3: 15, 4: 20}
        return DICT[self.index_resolution]
    
    def get_width_popup_table(self):
        DICT = {0: 62, 1: 125, 2 : 125, 3: 187, 4: 250}
        return DICT[self.index_resolution]
    
    def get_width_line_edit_stage_area(self):
        DICT = {0: 20, 1: 40, 2 : 40, 3: 60, 4: 80}
        return DICT[self.index_resolution]
    
    def get_size_popup_picture(self):
        DICT = {0: 150, 1: 300, 2 : 300, 3: 450, 4: 600}
        return DICT[self.index_resolution]
    
    def get_popup_position_height_multiplier(self):
        DICT = {0: 17, 1: 35, 2 : 35, 3: 52, 4: 70}
        return DICT[self.index_resolution]
        
    def get_title_size(self):
        TITLE_SIZE_DICT = {0: 10, 1: 20, 2 : 20, 3: 30, 4: 40}
        return str(TITLE_SIZE_DICT[self.index_resolution])
    
    def get_hspacing_working_folder(self):
        SPACING_WORKING_FOLDER_DICT = {0: 12, 1: 25, 2 : 25, 3: 37, 4: 50}
        return SPACING_WORKING_FOLDER_DICT[self.index_resolution]
    
    def get_hspacing_exposure(self):
        SPACING_WORKING_FOLDER_DICT = {0: 5, 1: 10, 2 : 10, 3: 15, 4: 20}
        return SPACING_WORKING_FOLDER_DICT[self.index_resolution]
    
    def get_vspacing_working_folder(self):
        SPACING_WORKING_FOLDER_DICT = {0: 15, 1: 30, 2 : 30, 3: 45, 4: 60}
        return SPACING_WORKING_FOLDER_DICT[self.index_resolution]
    
    def get_path_window_size(self):
        PATH_WINDOW_SIZE_DICT = {0: (150,50), 1: (300,100), 2 : (300,100), 3: (450,150), 4: (600,200)}
        return PATH_WINDOW_SIZE_DICT[self.index_resolution]
    
    def get_calibration_window_size(self):
        DICT = {0: (150,30), 1: (300,60), 2 : (300,60), 3: (450,90), 4: (600,120)}
        return DICT[self.index_resolution]
    
    def get_space_number_wafers_widget(self):
        SPACE_NUMBER_WAFER_DICT = {0: 12, 1: 25, 2 : 25, 3: 37 , 4: 50}
        return SPACE_NUMBER_WAFER_DICT[self.index_resolution]
    
    def get_width_number_wafers_line_edit(self):
        WIDTH_NUMBER_WAFER_LE_DICT = {0: 20, 1: 40, 2 : 40, 3: 60 , 4: 80}
        return WIDTH_NUMBER_WAFER_LE_DICT[self.index_resolution]
    
    def get_width_exposure_line_edit(self):
        WIDTH_EXPOSURE_LE_DICT = {0: 25, 1: 50, 2 : 50, 3: 75 , 4: 100}
        return WIDTH_EXPOSURE_LE_DICT[self.index_resolution]
    
    def get_width_gain_line_edit(self):
        WIDTH_GAIN_LE_DICT = {0: 20, 1: 40, 2 : 40, 3: 60 , 4: 80}
        return WIDTH_GAIN_LE_DICT[self.index_resolution]
    
    def get_vhspacing_step2(self):
        SPACE_STEP2_DICT = {0: 7, 1: 15, 2 : 15, 3: 22 , 4: 30}
        return SPACE_STEP2_DICT[self.index_resolution]
    
    def get_vhspacing_nosepiece_calibration(self):
        SPACE_CAL_DICT = {0: 2, 1: 5, 2 : 5, 3: 7 , 4: 10}
        return SPACE_CAL_DICT[self.index_resolution]
    
    def get_vspacing_nosepiece_calibration(self):
        SPACE_CAL_DICT = {0: 10, 1: 20, 2 : 20, 3: 30 , 4: 40}
        return SPACE_CAL_DICT[self.index_resolution]
    
    def get_hspacing_aspect_ratio(self):
        SPACE_AR_DICT = {0: 10, 1: 20, 2 : 20, 3: 30 , 4: 40}
        return SPACE_AR_DICT[self.index_resolution]
    
    def get_margin_step2(self):
        MARGIN_STEP2_DICT = {0: 7, 1: 15, 2 : 15, 3: 22 , 4: 30}
        return MARGIN_STEP2_DICT[self.index_resolution]
    
    def get_space_ai(self):
        SPACE_AI_DICT = {0: 15, 1: 30, 2 : 30, 3: 45 , 4: 60}
        return SPACE_AI_DICT[self.index_resolution]
    
    def get_width_thresold_line_edit(self):
        WIDTH_NUMBER_WAFER_LE_DICT = {0: 22, 1: 45, 2 : 30, 3: 45 , 4: 60}
        return WIDTH_NUMBER_WAFER_LE_DICT[self.index_resolution]
    
    def get_vspacing_scan_options(self):
        SPACING_SCAN_OPTIONS = {0: 7, 1: 15, 2 : 15, 3: 22, 4: 30}
        return SPACING_SCAN_OPTIONS[self.index_resolution]
    
    def get_vspacing_idcorner_options(self):
        DICT = {0: 7, 1: 15, 2 : 15, 3: 22, 4: 30}
        return DICT[self.index_resolution]
    
    def get_hspacing_scan_options(self):
        SPACING_SCAN_OPTIONS = {0: 15, 1: 30, 2 : 30, 3: 45, 4: 60}
        return SPACING_SCAN_OPTIONS[self.index_resolution]
    
    def get_minimum_vspacing_left_pannel(self):
        SPACING_LEFT_PANNEL = {0: 12, 1: 25, 2 : 25, 3: 37, 4: 25}
        return SPACING_LEFT_PANNEL[self.index_resolution]
    
    def get_minimum_vspacing_right_pannel(self):
        SPACING_RIGHT_PANNEL = {0: 12, 1: 25, 2 : 25, 3: 37, 4: 50}
        return SPACING_RIGHT_PANNEL[self.index_resolution]
    
    def get_small_left_margin(self):
        MARGIN_DICT = {0: 10, 1: 20, 2 : 20, 3: 30, 4: 40}
        return MARGIN_DICT[self.index_resolution]
    
    def get_hspacing_nosepiece(self):
        SPACING_NOSEPIECE_DICT = {0: 2, 1: 5, 2 : 5, 3: 7, 4: 10}
        return SPACING_NOSEPIECE_DICT[self.index_resolution]
    
    def get_objective_button_size(self):
        FONT_PAD_SIZE_DICT = {0: (2,7), 1: (5,15), 2 : (5,15), 3: (7,22), 4: (10,30)}
        return FONT_PAD_SIZE_DICT[self.index_resolution]
    
    def get_macro_button_size(self):
        FONT_PAD_SIZE_DICT = {0: (2,7), 1: (5,15), 2 : (5,15), 3: (7,22), 4: (10,30)}
        return FONT_PAD_SIZE_DICT[self.index_resolution]
    
    def get_small_button_size(self):
        DICT = {0: (2,7), 1: (5,15), 2 : (5,15), 3: (7,22), 4: (10,20)}
        return DICT[self.index_resolution]
    
    def get_gridspacing_calibration_information(self):
        DICT = {0: 12, 1: 25, 2 : 25, 3: 37, 4: 50}
        return DICT[self.index_resolution]
    
    def get_spacing_thickness_information(self):
        DICT = {0: 10, 1: 20, 2 : 20, 3: 30, 4: 40}
        return DICT[self.index_resolution]
    
    def get_width_thickness_information(self):
        DICT = {0: 30, 1: 60, 2 : 60, 3: 90, 4: 120}
        return DICT[self.index_resolution]
    
    def get_calibration_window_size(self):
        DICT = {0: (150,15), 1: (300,30), 2 : (300,30), 3: (450,45), 4: (600,120)}
        return DICT[self.index_resolution]
    
    def get_vspacing_information_AI(self):
        DICT = {0: 2, 1: 5, 2 : 5, 3: 8, 4: 10}
        return DICT[self.index_resolution]
    
    def get_width_option_offset(self):
        DICT = {0: 37, 1: 75, 2 : 75, 3: 112, 4: 150}
        return DICT[self.index_resolution]
    
    def get_push_button_size(self):
        DICT = {0: (7, 1, 5, 2, 4), 1: (13, 2, 10, 3, 9), 2 : (13, 2, 10, 3, 9), 3: (19, 2, 15, 4, 13), 4: (26, 3, 20, 6, 17)}
        return DICT[self.index_resolution]
    
    def get_dropdown_size(self):
        DICT = {0: (7, 1, 5, 2, 4), 1: (13, 2, 10, 3, 9), 2 : (13, 2, 10, 3, 9), 3: (19, 2, 15, 4, 13), 4: (26, 3, 20, 6, 17)}
        return DICT[self.index_resolution]
    
class Title(QtWidgets.QLabel):
    def __init__(self,window,scaling_resolution):
        super().__init__(window)
        font_size = scaling_resolution.get_title_size()
        self.setStyleSheet("font-size: "+font_size+"px;")
        
class Informator(QtWidgets.QLabel):
    def __init__(self,window,scaling_resolution):
        super().__init__(window)
        font_size = scaling_resolution.get_informator_size()
        self.setStyleSheet("font-size: "+font_size+"px;"
                           "background-color:transparent;"
                           "border: 1px solid #F4F1DE;"
                           )

class ObjectiveButton(QtWidgets.QPushButton):
    def __init__(self,window,scaling_resolution):
        super().__init__(window)
        
        values = scaling_resolution.get_push_button_size()
        self.border = values[1]
        self.border_hover = values[3]
        
        self.padding, self.font_size = scaling_resolution.get_objective_button_size()
        
        self.passive_state()
        
    def passive_state(self):
        self.setStyleSheet("""
ObjectiveButton
{
	background-color: transparent;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

ObjectiveButton::pressed
{
    background-color: #81B29A;
}

ObjectiveButton::hover
{
    border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding-self.border_hover+self.border)+"""px;
    
}

"""
)
    
    def active_state(self):
        self.setStyleSheet("""
ObjectiveButton
{
	background-color: #81B29A;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

ObjectiveButton::pressed
{
    background-color: #81B29A;
}

ObjectiveButton::hover
{
    border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding-self.border_hover+self.border)+"""px;
    
}

"""
)

class ToolButton(QtWidgets.QToolButton):
    def __init__(self,window, scaling_resolution):
        super().__init__(window)
        values = scaling_resolution.get_push_button_size()
        self.font_size = values[0]
        self.border = values[1]
        self.padding = values[2]
        self.border_hover = values[3]
        self.padding_hover = values[4]
        self.normal_state()
        
    def normal_state(self):
        self.setStyleSheet("""
ToolButton
{
	background-color: transparent;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

ToolButton::pressed
{
    background-color: #81B29A;
}

ToolButton::hover
{
    border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding_hover)+"""px;
    
}

"""
)
    
    def error_state(self):
        self.setStyleSheet("""
ToolButton
{
	background-color: #E07A5F;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

ToolButton::pressed
{
    background-color: #81B29A;
}

ToolButton::hover
{
    border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding_hover)+"""px;
    
}

"""
)

class MacroButton(QtWidgets.QPushButton):
    def __init__(self,window,scaling_resolution):
        super().__init__(window)
        padding, font_size = scaling_resolution.get_macro_button_size()
        self.setStyleSheet("font-size: "+str(font_size)+"px;"
                            "padding: "+str(padding)+"px;"
                            )

class SmallButton(QtWidgets.QPushButton):
    def __init__(self,window,scaling_resolution):
        super().__init__(window)
        padding, font_size = scaling_resolution.get_small_button_size()
        self.setStyleSheet("font-size: "+str(font_size)+"px;"
                            "padding: "+str(padding)+"px;"
                            )

class DropDown(QtWidgets.QComboBox):
    def __init__(self, window, scaling_resolution):
        super().__init__(window)
        values = scaling_resolution.get_dropdown_size()
        self.font_size = values[0]
        self.border = values[1]
        self.padding = values[2]
        self.border_hover = values[3]
        self.padding_hover = values[4]
        self.normal_state()
        
    def normal_state(self):
        self.setStyleSheet("""
QComboBox
{
	background-color: transparent;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

QComboBox::hover
{
	border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding_hover)+"""px;

}

QComboBox QAbstractItemView
{
  selection-background-color: #81B29A;
}

QComboBox::drop-down
{
	border : 0px;
}
"""
)

# QComboBox::down-arrow
# {
# 	image: url(Icons/down_arrow.png);
#     width: 35px;
#     height: 90px;
#     left: -15px;
# }

    
    def error_state(self):
        self.setStyleSheet("""
QComboBox
{
	background-color: #E07A5F;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}
"""
)

class PushButton(QtWidgets.QPushButton):
    def __init__(self,window, scaling_resolution):
        super().__init__(window)
        values = scaling_resolution.get_push_button_size()
        self.font_size = values[0]
        self.border = values[1]
        self.padding = values[2]
        self.border_hover = values[3]
        self.padding_hover = values[4]
        self.normal_state()
        
    def normal_state(self):
        self.setStyleSheet("""
PushButton
{
	background-color: transparent;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

PushButton::pressed
{
    background-color: #81B29A;
}

PushButton::hover
{
    border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding_hover)+"""px;
    
}

"""
)
    
    def error_state(self):
        self.setStyleSheet("""
PushButton
{
	background-color: #E07A5F;
	color: #FEFEFD;
	font-size: """+str(self.font_size)+"""px;
	font-weight: bold;
	border: """+str(self.border)+"""px solid #81B29A;
	border-radius: 0px;
	padding: """+str(self.padding)+"""px;

}

PushButton::pressed
{
    background-color: #81B29A;
}

PushButton::hover
{
    border: """+str(self.border_hover)+"""px solid #81B29A;
    padding: """+str(self.padding_hover)+"""px;
    
}

"""
)
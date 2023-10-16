import pymmcore
import cv2
import warnings
import os.path
import numpy as np
import skimage.measure
from time import sleep

#this is a comment

TARGET_BKG = 180.

class _Camera():
    def __init__(self, mmc):
        self.mmc = mmc
        self.name = self.mmc.getCameraDevice()
        self.check_binning_configuration()
        self.bgr_correction = np.asarray([1.,1.,1.])
        
        self.mmc.setConfig('AutoExposure','Manual')
        
        #get camera ranges
        self.MINIMUM_EXPOSURE, self.MAXIMUM_EXPOSURE = self.get_exposure_range()
        self.MINIMUM_GAIN, self.MAXIMUM_GAIN = self.get_gain_range()

        #define limits
        self.SOFT_MAXIMUM_EXPOSURE = 250
        self.HARD_MAXIMUM_EXPOSURE = 5000
        self.SOFT_MAXIMUM_GAIN = self.MAXIMUM_GAIN * 0.5
        self.HARD_MAXIMUM_GAIN = self.MAXIMUM_GAIN
    
        self.MIN_MAX_BLUE = [float(self.mmc.getPropertyLowerLimit(self.name, "WhiteBalanceBlue")),float(self.mmc.getPropertyUpperLimit(self.name, "WhiteBalanceBlue"))]
        self.MIN_MAX_RED = [float(self.mmc.getPropertyLowerLimit(self.name, "WhiteBalanceRed")),float(self.mmc.getPropertyUpperLimit(self.name, "WhiteBalanceRed"))]
        
        self.MEDIUM_BLUE = (self.MIN_MAX_BLUE[0]+self.MIN_MAX_BLUE[1])/2
        self.MEDIUM_RED = (self.MIN_MAX_RED[0]+self.MIN_MAX_RED[1])/2
        
    def _get_most_probable_intensity(self):
        image = self.snap_image()
        return np.median(image)
    
    def _set_next_auto_exposure_target(self, correction_coefficient, old_exposure, old_gain):
        
        new_gain, new_exposure = old_gain, old_exposure
        
        zone1 = old_exposure < self.SOFT_MAXIMUM_EXPOSURE and old_gain == self.MINIMUM_GAIN
        zone2 = old_exposure >= self.SOFT_MAXIMUM_EXPOSURE and old_gain >= self.MINIMUM_GAIN and old_gain < self.SOFT_MAXIMUM_GAIN 
        zone3 = old_exposure >= self.SOFT_MAXIMUM_EXPOSURE and old_gain >= self.SOFT_MAXIMUM_GAIN
                
        if zone1 :
            new_exposure = np.round(old_exposure * correction_coefficient,1)
            if new_exposure >= self.SOFT_MAXIMUM_EXPOSURE : new_exposure = self.SOFT_MAXIMUM_EXPOSURE
            if new_exposure <= self.MINIMUM_EXPOSURE : new_exposure = self.MINIMUM_EXPOSURE
            return new_gain, new_exposure
        
        if zone2 :
            new_gain = old_gain * correction_coefficient
            if new_gain >= self.SOFT_MAXIMUM_GAIN : new_gain = self.SOFT_MAXIMUM_GAIN
            if new_gain <= self.MINIMUM_GAIN : new_gain = self.MINIMUM_GAIN
            return new_gain, new_exposure
        
        if zone3 :
            new_gain = old_gain * np.sqrt(correction_coefficient)
            new_exposure = old_exposure * np.sqrt(correction_coefficient)
            if new_exposure > self.HARD_MAXIMUM_EXPOSURE:
                new_exposure = self.HARD_MAXIMUM_EXPOSURE
                new_gain = new_gain * np.sqrt(correction_coefficient)
            if new_gain > self.SOFT_MAXIMUM_GAIN:
                new_gain = self.HARD_MAXIMUM_GAIN
                new_exposure = new_exposure * np.sqrt(correction_coefficient)
            if new_exposure < self.SOFT_MAXIMUM_EXPOSURE:
                new_exposure = self.SOFT_MAXIMUM_EXPOSURE
        
        return new_gain, new_exposure


    def auto_exposure(self):
        #go at "low" exposure time (~10 fps) and low gain
        # self.set_exposure(10)
        self.set_gain(self.MINIMUM_GAIN)

        # difference_in_exposure , difference_in_gain = 1e10 , 1e10
        most_probable_intensity = self._get_most_probable_intensity()
        if most_probable_intensity == 0 : most_probable_intensity = 1
        correction_coefficient = TARGET_BKG/most_probable_intensity
        
        count = 0
        while np.abs(correction_coefficient-1)>0.03 and count < 10:
            old_exposure = self.get_exposure()
            old_gain = self.get_gain()
            
            new_gain, new_exposure = self._set_next_auto_exposure_target(correction_coefficient, old_exposure, old_gain)
                        
            self.set_gain(np.round(new_gain,1))
            self.set_exposure(np.round(new_exposure,1))
            
            sleep(0.1+(new_exposure)*2/1000)
            
            most_probable_intensity = self._get_most_probable_intensity()
            if most_probable_intensity == 0 : most_probable_intensity = 1
            correction_coefficient = TARGET_BKG/most_probable_intensity
            
            print(most_probable_intensity, new_exposure, new_gain)
            count += 1
            
    
    def auto_exposure_smart(self):
        #go at "low" exposure time (~10 fps) and low gain
        # self.set_exposure(10)
        # self.set_gain(self.MINIMUM_GAIN)

        # difference_in_exposure , difference_in_gain = 1e10 , 1e10
        most_probable_intensity = self._get_most_probable_intensity()
        if most_probable_intensity == 0 : most_probable_intensity = 1
        correction_coefficient = TARGET_BKG/most_probable_intensity
        
        x_exp = []
        y_val = []
        count = 0
        
        if np.abs(most_probable_intensity - 127) < 70:
            x_exp.append(self.get_exposure())
            y_val.append(most_probable_intensity)
            count = 1       
        
        while True:
            
            old_exposure = self.get_exposure()
            old_gain = self.get_gain()
            
            print(count, old_exposure, most_probable_intensity)
            
            new_gain, new_exposure = self._set_next_auto_exposure_target(correction_coefficient, old_exposure, old_gain)
                        
            self.set_gain(np.round(new_gain,1))
            self.set_exposure(np.round(new_exposure,1))
            
            sleep(0.2+(new_exposure)*2/1000)
            
            most_probable_intensity = self._get_most_probable_intensity()
            if most_probable_intensity == 0 : most_probable_intensity = 1
            correction_coefficient = TARGET_BKG/most_probable_intensity
            
            if np.abs(most_probable_intensity-127)<=2.5:
                break
            
            if np.abs(most_probable_intensity - 127) < 70:
                x_exp.append(self.get_exposure())
                y_val.append(most_probable_intensity)
                count += 1
            
            if count == 4:
                pol = np.poly1d(np.polyfit(y_val,x_exp,1))
                self.set_exposure(np.round(pol(127),1))
                break
    
    def auto_white(self):
        
        if float(self.mmc.getProperty(self.name, "WhiteBalanceBlue")) < 5:
            self.mmc.setProperty(self.name, "WhiteBalanceBlue", str(int(np.round(self.MEDIUM_BLUE,0))))
        if float(self.mmc.getProperty(self.name, "WhiteBalanceRed")) < 5:
            self.mmc.setProperty(self.name, "WhiteBalanceRed", str(int(np.round(self.MEDIUM_RED,0))))
        
        image = self.snap_image()
        r,g,b = cv2.split(image)

        most_probable_blue_value = np.median(b)
        most_probable_green_value = np.median(g)
        most_probable_red_value = np.median(r)
        
        count = 0
        while count < 10 and (np.abs(most_probable_blue_value - most_probable_green_value) >= 1.5 or np.abs(most_probable_red_value - most_probable_green_value) >= 1.5):
            sleep(0.2)
            actual_blue_balance_value = float(self.mmc.getProperty(self.name, "WhiteBalanceBlue"))
            actual_red_balance_value = float(self.mmc.getProperty(self.name, "WhiteBalanceRed"))
        
            image = self.snap_image()
            r,g,b = cv2.split(image)

            most_probable_blue_value = np.median(b)
            most_probable_green_value = np.median(g)
            most_probable_red_value = np.median(r)

            #prevent division by 0
            if most_probable_blue_value == 0 : most_probable_blue_value+=1
            if most_probable_green_value == 0 : most_probable_green_value+=1
            if most_probable_red_value == 0 : most_probable_red_value+=1
        
            new_blue_balance_value = float(most_probable_green_value) /  most_probable_blue_value * actual_blue_balance_value
            new_red_balance_value = float(most_probable_green_value) / most_probable_red_value * actual_red_balance_value
            
            new_blue_balance_value = min(new_blue_balance_value, 799)
            new_red_balance_value = min(new_red_balance_value, 799)
            
            self.mmc.setProperty(self.name, "WhiteBalanceBlue", str(int(np.round(new_blue_balance_value,0))))
            self.mmc.setProperty(self.name, "WhiteBalanceRed", str(int(np.round(new_red_balance_value,0))))
            
            count+=1
            print(count,np.abs(most_probable_blue_value - most_probable_green_value),np.abs(most_probable_red_value - most_probable_green_value))
            
    def bin_image(self):
        self.mmc.stopSequenceAcquisition()
        self.mmc.setConfig('Binning','True')
        self.mmc.startContinuousSequenceAcquisition(1)
        

    def check_binning_configuration(self):
        ## For Microscope to function correctly, a group called 'Binning' has to be created in micromanager.
        ## This group shall contain two presets: True and False.
        ## If you don't have this group, binning will not be performed
        exception_line1 = "The groups in micromanager have not been setup properly.\n"
        exception_line2 = "You should create a group called 'Binning' with two presets: True and False.\n"
        exception_line3 = "If you don't have this group, binning will not be performed.\n"
        exception_line4 = "Even in that case all should be okay.\n"
        message = exception_line1+exception_line2+exception_line3+exception_line4

        binning_config = self.mmc.getAvailableConfigs('Binning')
        expected_binning_config = ('False','True')

        if binning_config != expected_binning_config:    
            warnings.warn(message)
    
    def color_correct(self,image):
        image = image * self.bgr_correction
        image[image>255] = 255
        image = np.uint8(image)
        return image

    def compute_white_balance_coefficient(self):
        image = self.snap_image()
        histogram_blue_channel = cv2.calcHist([image],[0],None,[256],[0,256])
        histogram_green_channel = cv2.calcHist([image],[1],None,[256],[0,256])
        histogram_red_channel = cv2.calcHist([image],[2],None,[256],[0,256])

        most_probable_blue_value = np.argmax(histogram_blue_channel)
        most_probable_green_value = np.argmax(histogram_green_channel)
        most_probable_red_value = np.argmax(histogram_red_channel)

        #prevent division by 0
        if most_probable_blue_value == 0 : most_probable_blue_value+=1
        if most_probable_green_value == 0 : most_probable_green_value+=1
        if most_probable_red_value == 0 : most_probable_red_value+=1

        #change the bgr_correction array values
        self.bgr_correction[0] = TARGET_BKG/most_probable_blue_value
        self.bgr_correction[1] = TARGET_BKG/most_probable_green_value
        self.bgr_correction[2] = TARGET_BKG/most_probable_red_value
        

    def full_resolution(self):
        self.mmc.stopSequenceAcquisition()
        self.mmc.setConfig('Binning','False')
        self.mmc.startContinuousSequenceAcquisition(1)
        
    def get_exposure(self):
        exposure = self.mmc.getExposure()
        return exposure
    
    def get_exposure_range(self):
        minimum_exposure = self.mmc.getPropertyLowerLimit(self.name,'Exposure')
        maximum_exposure = self.mmc.getPropertyUpperLimit(self.name,'Exposure')
        return minimum_exposure, maximum_exposure

    def get_gain(self):
        gain = self.mmc.getProperty(self.name,'Gain')
        return float(gain)

    def get_gain_range(self):
        minimum_gain = self.mmc.getPropertyLowerLimit(self.name,'Gain')
        maximum_gain = self.mmc.getPropertyUpperLimit(self.name,'Gain')
        return minimum_gain, maximum_gain

    def is_binned(self):
        binning = self.mmc.getCurrentConfig('Binning')
        return binning == 'True'

    def set_exposure(self, exposure_target):
        self.mmc.setExposure(exposure_target)
    
    def set_gain(self, gain_target):
        self.mmc.setProperty(self.name,'Gain',str(gain_target))

    def snap_image(self):
        # actualize the captor
        # get the image from buffer
        # return the image
        while self.mmc.getRemainingImageCount() == 0:
            sleep(0.1/1000)
        image = self.mmc.getLastImage()
        
        image_height, image_width = image.shape
        image = image.view("uint8") #convert to 4, 8 bits channel
        image = image.reshape((image_height,image_width, 4))
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR) #convert from RGBA to BGR
        return image
    
    def snap_slow(self):
        self.mmc.snapImage()
        image = self.mmc.getImage()
        
        image_height, image_width = image.shape
        image = image.view("uint8") #convert to 4, 8 bits channel
        image = image.reshape((image_height,image_width, 4))
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR) #convert from RGBA to BGR
        return image

    

class _Objective():
    def __init__(self,mmc):
        self.mmc = mmc
        self.number_of_objectives = self.get_number_of_objectives()
        self.check_objective_configuration() 
        self.objective_names = self.get_available_objective_names()
    
    def check_objective_configuration(self):
        ## For Microscope to function correctly, a group called 'Objective' has to be created in micromanager.
        ## This group shall contain the different objectives availables and calibration should be associated to them.
        ## If the turret is manual, if there is only one objective or if the turret is not controlable with micromanager,
        ## A Demo Turret (DTurret) from the DemoCamera Device Adapter should be added and configured with the objective availables.
        if self.number_of_objectives == 0:
            exception_line1 = "The groups in micromanager have not been setup properly.\n"
            exception_line2 = "You should create a group called 'Objective' with your available objectives and associated calibrations.\n"
            exception_line3 = "If you only have one objective or a manual turret, please add the DTurret from the DemoCamera provided by macromanager.\n"
            raise Exception(exception_line1+exception_line2+exception_line3)

    def get_available_objective_names(self):
        objective_names = self.mmc.getAvailableConfigs('Objective')
        return objective_names

    def get_number_of_objectives(self):
        number_of_objectives = len(self.mmc.getAvailableConfigs('Objective'))
        return number_of_objectives

    def get_objective(self):
        current_objective_name = self.mmc.getCurrentConfig('Objective')
        return current_objective_name
    
    def set_objective(self,name):
        if name in self.objective_names:
            self.mmc.setConfig('Objective',name)
            return 0
        exception_line1 = "The name of the objective provided is not in the availables names for this microscope.\n"
        exception_line2 = "Check your micromanager 'Objective' Preset and chose a name that is listed there.\n"
        raise Exception(exception_line1 + exception_line2)

class _Stage():
    def __init__(self,mmc):
        self.mmc = mmc
        self.z_stage = self.mmc.getFocusDevice()
        self.xy_stage = self.mmc.getXYStageDevice()
        # self.mmc.setProperty(self.xy_stage, "Speed", 20000)
        # self.mmc.setProperty(self.xy_stage, "StartSpeed", 4000)
        # self.mmc.setProperty(self.xy_stage, "Acceleration", 1)
        
        
    def set_as_origin(self):
        self.mmc.setOriginXY()
    
    def initialise_stage(self):
        self.set_stage_position_xy(1e7,1e7)
        self.mmc.waitForDevice(self.xy_stage)
        sleep(0.5)
        self.set_as_origin()
    
    def get_stage_position_xy(self):
        x_position = self.mmc.getXPosition()
        y_position = self.mmc.getYPosition()
        return x_position, y_position

    def get_stage_position_z(self):
        z_position = self.mmc.getPosition(self.z_stage)
        return  z_position
    
    def move_relative_xy(self, delta_x, delta_y):
        x_position, y_position = self.get_stage_position_xy()
        x_target = x_position + delta_x
        y_target = y_position + delta_y
        self.set_stage_position_xy(x_target, y_target)

    def move_relative_z(self, delta_z):
        z_position = self.get_stage_position_z()
        z_target = z_position + delta_z
        self.set_stage_position_z(z_target)

    def set_stage_position_xy(self, x_target, y_target):
        self.mmc.setXYPosition(self.xy_stage, x_target, y_target)

    def set_stage_position_z(self, z_target):
        self.mmc.setPosition(self.z_stage, z_target)
    
    def wait_stage(self):
        self.mmc.waitForDevice(self.z_stage)
    
    def wait_stage_xy(self):
        self.mmc.waitForDevice(self.xy_stage)

class Microscope():
    """
    A pymmcore wraper with the essential functions needed to control the microscope in the context of flake hunting, or scanning large wafer in general.
    There is no parameters as relevant information will be pulled from the micromanager configuration.
    Be sure to set up your microscope correctly in micromanager
    """
    def __init__(self,micromanager_directory,micromanager_configuration_file, current_objective):
        self.mmc = pymmcore.CMMCore()
        self.mmc.setDeviceAdapterSearchPaths([micromanager_directory])
        self.mmc.loadSystemConfiguration(os.path.join(micromanager_directory, micromanager_configuration_file))
        
        self.mmc.setCircularBufferMemoryFootprint(1024)
        self.mmc.startContinuousSequenceAcquisition(1)
        sleep(0.5)
        
        self.mmc.setTimeoutMs(10000)
        
        self.camera = _Camera(self.mmc)
        self.objective = _Objective(self.mmc)
        self.stage = _Stage(self.mmc)
        
        #set captor to full resolution
        #this will load the field of view size self.field_of_view_micron
        self.full_resolution()
        #set the current objective
        #this will also load the field of view size self.field_of_view_micron
        self.set_objective(current_objective)
        
    
    def close_connection(self):
        self.mmc.stopSequenceAcquisition()
        self.mmc.clearCircularBuffer()
        self.mmc.unloadAllDevices()
    
    def continuous_focus(self):
        #get binning status of the camera and bin if it's not binned
        #use the camera binning method, because we don't want to lose time taking a snap and changing the field of view value, do we?
        
        is_binned = self.camera.is_binned()
        if not is_binned :
            self.camera.bin_image()
        
        z_position = self.stage.get_stage_position_z()
        
        while self.mmc.getRemainingImageCount() == 0:
            sleep(0.01)
        
        image = self.camera.snap_image()
        sharpness_score = self.get_sharpness_score(image)
        n_sharpness_score = sharpness_score + 1e-9
        
        step = 200
        while n_sharpness_score > sharpness_score:
            sharpness_score = n_sharpness_score
            z_position += step
            self.stage.set_stage_position_z(z_position)
            self.stage.wait_stage()
            image = self.camera.snap_image()
            n_sharpness_score = self.get_sharpness_score(image)
        
        n_sharpness_score = sharpness_score + 1e-9
        while n_sharpness_score > sharpness_score:
            sharpness_score = n_sharpness_score
            z_position -= step
            self.stage.set_stage_position_z(z_position)
            self.stage.wait_stage()
            image = self.camera.snap_image()
            n_sharpness_score = self.get_sharpness_score(image)
        
        z_position += step
        self.stage.set_stage_position_z(z_position)
        self.stage.wait_stage()
            
        #take a snap, color_correct it and extract sharpness score, then move to next z_step
        sharpness_score = []
        z_position = np.linspace(z_position-300,z_position+300, 10)
        
        for z in z_position:
            self.stage.set_stage_position_z(z)
            self.stage.wait_stage()
            image = self.camera.snap_image()
            image = self.camera.color_correct(image)
            sharpness_score.append(self.get_sharpness_score(image))
        
        sharpness_score = np.asarray(sharpness_score)
        
        pol = np.poly1d(np.polyfit(z_position, sharpness_score, 2))
        
        x=np.linspace(z_position[0],z_position[-1],10000)
        # plt.plot(x,pol(x),'k-')
        # plt.plot(z_position, sharpness_score, 'bo')
        
        in_focus_position = x[np.argmax(pol(x))]
        
        #get the z where the sharpness score is maximum
        # indice_of_maximum_sharpness = np.argmax(sharpness_score)
        # in_focus_position = z_position[indice_of_maximum_sharpness]

        #go to the z of maximum sharpness
        self.stage.set_stage_position_z(in_focus_position-100)
        self.stage.wait_stage()
        self.stage.set_stage_position_z(in_focus_position)
        
        #go back to initial binning status
        if not is_binned :
            self.camera.full_resolution()
    
    def auto_focus(self,micron_range,number_of_steps):
        #get binning status of the camera and bin if it's not binned
        #use the camera binning method, because we don't want to lose time taking a snap and changing the field of view value, do we?
        is_binned = self.camera.is_binned()
        if not is_binned :
            self.camera.bin_image()
        
        origin = self.stage.get_stage_position_z()
        
        #take a snap, color_correct it and extract sharpness score, then move to next z_step
        sharpness_score = []
        z_position = np.linspace(origin-micron_range/2,origin+micron_range/2, number_of_steps)
        
        self.stage.set_stage_position_z(z_position[0])
        self.stage.wait_stage()
        
        for z in z_position:
            self.stage.set_stage_position_z(z)
            self.stage.wait_stage()
            image = self.camera.snap_image()
            #image = self.camera.color_correct(image)
            sharpness_score.append(self.get_sharpness_score(image))
        
        sharpness_score = np.asarray(sharpness_score)
        z_position = np.asarray(z_position)
    
        #get the z where the sharpness score is maximum
        # indice_of_maximum_sharpness = np.argmax(sharpness_score)
        # in_focus_position = z_position[indice_of_maximum_sharpness]
        
        
        x=np.linspace(z_position[0],z_position[-1],10000)
        pol = np.poly1d(np.polyfit(z_position, sharpness_score, 4))
        # plt.plot(x,pol(x),'k-')
        # plt.plot(z_position, sharpness_score, 'bo')
        
        in_focus_position = x[np.argmax(pol(x))]
        
        #go to the z of maximum sharpness
        self.stage.set_stage_position_z(in_focus_position-50)
        self.stage.wait_stage()
        self.stage.set_stage_position_z(in_focus_position)
        self.stage.wait_stage()

        #go back to initial binning status
        if not is_binned :
            self.camera.full_resolution()
        
        return in_focus_position, np.max(pol(x))
    
    
    def fine_focus(self,micron_range,number_of_steps):
        #get binning status of the camera and bin if it's not binned
        #use the camera binning method, because we don't want to lose time taking a snap and changing the field of view value, do we?
        is_binned = self.camera.is_binned()
        if not is_binned :
            self.camera.bin_image()
        
        origin = self.stage.get_stage_position_z()
        
        #take a snap, color_correct it and extract sharpness score, then move to next z_step
        sharpness_score = []
        z_position = np.linspace(origin-micron_range/2,origin+micron_range/2, number_of_steps)
        
        
        self.stage.set_stage_position_z(z_position[0])
        self.stage.wait_stage()
        
        for z in z_position:
            self.stage.set_stage_position_z(z)
            self.stage.wait_stage()
            image = self.camera.snap_image()
            #image = self.camera.color_correct(image)
            sharpness_score.append(self.get_sharpness_score(image))
        
        sharpness_score = np.asarray(sharpness_score)
        z_position = np.asarray(z_position)
        
        # plt.plot(z_position, sharpness_score, 'bo')
        
        #get the z where the sharpness score is maximum
        indice_of_maximum_sharpness = np.argmax(sharpness_score)
        in_focus_position = z_position[indice_of_maximum_sharpness]
        
        #go to the z of maximum sharpness
        self.stage.set_stage_position_z(in_focus_position-50)
        self.stage.wait_stage()
        self.stage.set_stage_position_z(in_focus_position)
        self.stage.wait_stage()

        #go back to initial binning status
        if not is_binned :
            self.camera.full_resolution()
        
        return in_focus_position, np.max(sharpness_score)
    
    def bin_image(self):
        self.camera.bin_image()
        self.field_of_view_micron = self.get_field_of_view_micron()
    
    def full_resolution(self):
        self.camera.full_resolution()
        self.field_of_view_micron = self.get_field_of_view_micron()

    def get_field_of_view_micron(self):
        pixel_size = self.get_pixel_size()
        height_in_pixels, width_in_pixels, number_of_channel = self.camera.snap_image().shape
        height_in_micron = height_in_pixels*pixel_size
        width_in_micron = width_in_pixels*pixel_size
        return height_in_micron, width_in_micron
    
    def get_pixel_size(self):
        pixel_size = self.mmc.getPixelSizeUm()
        return pixel_size
    
    def get_sharpness_score(self,image):
        #perform a maxPooling on the image with 5px*5px*1channel clusters
        image = skimage.measure.block_reduce(image, (5,5,1), np.max)

        #get the derivative along x and y directions
        sobx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
        soby = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
        image = ( np.abs(sobx) + np.abs(soby) ) / 2

        #perform again a maxPooling on the derivated image with 5pc*5pc*3channels cluster
        image = skimage.measure.block_reduce(image, (5,5,3), np.max)

        #return the mean of the pooled derivative
        sharpness_score = np.mean(image)
        return sharpness_score

    def move_by_percent_field_of_view_x(self, percent):
        self.stage.move_relative_xy(percent*self.field_of_view_micron[1],0)

    def move_by_percent_field_of_view_y(self, percent):
        self.stage.move_relative_xy(0,percent*self.field_of_view_micron[0])

    def save_image(self,image,path):
        cv2.imwrite(path,image)

    def set_acquisition_path(self, path):
        if os.path.exists(path):
            self.path = path
            return 0
        raise Exception("The specified path do not exists")
    
    def set_objective(self,name):
        self.objective.set_objective(name)
        self.field_of_view_micron = self.get_field_of_view_micron()

###to be done

#profile correction (put this in another file?)
    #polynomial fit
    #background reconstruction algo
    #use stocked background picture
    #use stocked background picture and fit it

##ML_auto_exposure
##ML_white_balance
##ML_auto_focus

    
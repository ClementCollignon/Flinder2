# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
        
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 20
FONT_THICKNESS = 70
BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)
WAFER_NUMBER_COLOR = (129,178,154)
     
FOV = [2842.9,1890.6] #um

FOV[0] /= 4
FOV[1] /= 4

OVERLAP = 0.05 #%
TRAVEL = [FOV[0]*(1-OVERLAP), FOV[1]*(1-OVERLAP)] #um

STAGE_PX_SIZE = 10 #um/px
QUICK_SCAN_STEP = 2000 #um

N_FOCUS = 20

def find_large_contours(mat_stage):
    contours, hierarchy = cv2.findContours(mat_stage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    large_contours = []
    for i,contour in enumerate(contours):
        if cv2.contourArea(contour) > 1e6:
            contour = cv2.approxPolyDP(contour,0.005*cv2.arcLength(contour,True),True)
            contour = cv2.convexHull(contour)
            cv2.drawContours(mat_stage, [contour], -1, (255,255,255), thickness=cv2.FILLED)
            large_contours.append(contour)
        
    return large_contours

def draw_wafer_numbers(large_contours, h, w):
    mask = np.zeros((h, w, 3), dtype = np.uint8)
    cv2.drawContours(mask, large_contours, -1, (120,120,120), thickness=cv2.FILLED)
        
    for wafer_number, contour in enumerate(large_contours):
        rect = cv2.minAreaRect(contour)
        position = (int(rect[0][0]),int(rect[0][1]))
        text = str(wafer_number)
            
        textsize = cv2.getTextSize(text, FONT, FONT_SCALE, FONT_THICKNESS)[0]
        tupple_position=(int(position[0] - textsize[0]/2),int(position[1] + textsize[1]/2))
        
        x,y,wr,hr = cv2.boundingRect(contour)
        
        margin = int(QUICK_SCAN_STEP/STAGE_PX_SIZE/2)
        
        xmin = max(x-margin,0)
        ymin = max(y-margin,0)
        xmax = min(x+wr+margin,w)
        ymax = min(y+hr+margin,h)
        
        
        
        cv2.rectangle(mask, (xmin, ymin), (xmax, ymax), (255,0,0), 4)
        cv2.putText(mask ,text , tupple_position, FONT, FONT_SCALE, WAFER_NUMBER_COLOR, FONT_THICKNESS)
        
        translate_x = TRAVEL[0]/STAGE_PX_SIZE
        translate_y = TRAVEL[1]/STAGE_PX_SIZE
        
        X = xmin
        Y = ymin
        
        pt = 5
        limit_um = (FOV[0]/STAGE_PX_SIZE)/2 + (QUICK_SCAN_STEP/STAGE_PX_SIZE)/2
        
        pos_list = []
        focus_list = []
        XY = []
        
        while Y <= ymax: 
            while X <= xmax:
                X+=translate_x
                if cv2.pointPolygonTest(contour, (X,Y), True) > -limit_um:
                    mask[int(Y-pt):int(Y+pt), int(X-pt):int(X+pt)] = [0,255,0]
                    pos_list.append((X*STAGE_PX_SIZE,Y*STAGE_PX_SIZE))
                if cv2.pointPolygonTest(contour, (X,Y), True) > 0:
                    mask[int(Y-pt):int(Y+pt), int(X-pt):int(X+pt)] = [255,0,0]
                    focus_list.append((X*STAGE_PX_SIZE,Y*STAGE_PX_SIZE))
                    XY.append((int(X),int(Y)))
                
            Y+=translate_y
            while X >= xmin:
                X-=translate_x
                if cv2.pointPolygonTest(contour, (X,Y), True) > -limit_um:
                    mask[int(Y-pt):int(Y+pt), int(X-pt):int(X+pt)] = [0,255,0]
                    pos_list.append((X*STAGE_PX_SIZE,Y*STAGE_PX_SIZE))
                if cv2.pointPolygonTest(contour, (X,Y), True) > 0:
                    mask[int(Y-pt):int(Y+pt), int(X-pt):int(X+pt)] = [255,0,0]
                    focus_list.append((X*STAGE_PX_SIZE,Y*STAGE_PX_SIZE))
                    XY.append((int(X),int(Y)))
            Y+=translate_y
        
        N = len(focus_list)
        pt = 20
        
        i=0
        val = []

        while i < N_FOCUS:
            ii = np.random.randint(0,N)
            if ii not in val:
                mask[int(XY[ii][1]-pt):int(XY[ii][1]+pt), int(XY[ii][0]-pt):int(XY[ii][0]+pt)] = [0,0,255]
                val.append(ii)
                i+=1
        
        val = np.asarray(val)
        focus_list = np.asarray(focus_list)
        val = np.sort(val)
        
        focus_list = focus_list[val]
        
        
            
            
    return mask
         
mat_stage = cv2.imread("wafers_position.jpg")
mat_stage = cv2.cvtColor(mat_stage, cv2.COLOR_RGB2GRAY)
h, w = mat_stage.shape
        
large_contours = find_large_contours(mat_stage)
mask = draw_wafer_numbers(large_contours, h, w)

plt.imshow(mask)
    

    

        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
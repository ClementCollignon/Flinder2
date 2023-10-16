# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:24:59 2021

@author: Nikon-fablab
"""

import time
# from microscope import Microscope
from matplotlib import pyplot as plt
import numpy as np
import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 20
FONT_THICKNESS = 70
BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)
BLUE_COLOR = (0,0,255)

image = cv2.imread("wafers_position.jpg")

image_g = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

contours, hierarchy = cv2.findContours(image_g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

nice_contour = []
wafers = []
for i,contour in enumerate(contours):
    if cv2.contourArea(contour) > 1e6:
        contour = cv2.approxPolyDP(contour,0.005*cv2.arcLength(contour,True),True)
        wafers.append(contour)
        contour = cv2.convexHull(contour)
        
        cv2.drawContours(image, [contour], -1, (255,255,255), thickness=cv2.FILLED)
        
        nice_contour.append(contour)


mask=np.zeros(image_g.shape, dtype = np.uint8)
cv2.drawContours(mask, nice_contour, -1, 255, thickness=cv2.FILLED)

mask2=np.zeros(image.shape, dtype = np.uint8)
cv2.drawContours(mask2, nice_contour, -1, (180,180,180), thickness=cv2.FILLED)

for wafer_number, contour in enumerate(nice_contour):

    rect = cv2.minAreaRect(contour)
    position = (int(rect[0][0]),int(rect[0][1]))
    
    text = str(wafer_number)
    
    textsize = cv2.getTextSize(text, FONT, FONT_SCALE, FONT_THICKNESS)[0]
    tupple_position=(int(position[0] - textsize[0]/2),int(position[1] + textsize[1]/2))
    
    cv2.putText(mask2 ,text , tupple_position, FONT, FONT_SCALE, BLUE_COLOR, FONT_THICKNESS)

#print(mask)


#cv2.CHAIN_APPROX_SIMPLE

plt.imshow(mask2)
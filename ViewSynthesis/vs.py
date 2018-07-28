# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:38:37 2018

@author: dues1
"""

#view Synthesis
import numpy as np
import cv2

view1 = cv2.imread('C:/Documents-Summer2018/CVIP/PA2/view1.png')
view5 = cv2.imread('C:/Documents-Summer2018/CVIP/PA2/view5.png')
gt1 = cv2.imread('C:/Documents-Summer2018/CVIP/PA2/disp1.png',0)
gt5 = cv2.imread('C:/Documents-Summer2018/CVIP/PA2/disp5.png',0)


view3_left = np.zeros((view1.shape))

view3_right = np.zeros((view5.shape))
print(gt1.shape,view1.shape,view5.shape,view3_left.shape)
print(gt1)

#print(view1.shape,view3_left.shape,view5.shape)

row = view1.shape[0]
col = view1.shape[1]

#view3generated from view1

for i in range(0,row):     
    for j in range(0,col):
        shift = gt1[i][j]//2
        shifted_pixel = j - shift;
#        print(shifted_pixel)
        if(shifted_pixel < 0):
            continue;#do nothing      
#        print(view3_left[i][shifted_pixel])
#        print(view1[i][j])
       
        view3_left[i][shifted_pixel] = view1[i][j]
        
cv2.imshow("View3 genereated from Shifting View1 to left",view3_left)# / view3_left.max())
cv2.imwrite('view3_left.jpg',view3_left)
for i in range(0,row):     
    for j in range(0,col):
        shift = gt5[i][j]//2
        shifted_pixel = j + shift;
        if(shifted_pixel > col-1):
            continue;#do nothing
            
        if(view3_left[i][shifted_pixel].all() == 0):
            view3_right[i][shifted_pixel] = view5[i][j]
            view3_left[i][shifted_pixel] = view5[i][j]
            
cv2.imshow("View3 genereated from Shifting View1 to right",view3_right / 255)
cv2.imwrite('view3_right.jpg',view3_right)

cv2.imshow("Final view3",view3_left / 255) 
           
cv2.imwrite('view3fin.jpg',view3_left)

            
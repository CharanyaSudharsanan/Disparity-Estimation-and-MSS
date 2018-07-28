# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:36:40 2018

@author: dues1
"""

import numpy as np
import cv2

left_img = cv2.imread('view1.png', 0)  #read it as a grayscale image
right_img = cv2.imread('view5.png', 0)

#print(left_img)
#Disparity Computation for Left Image

M_left=np.zeros(left_img.shape)
M_left=M_left.astype(int)
M_right=np.zeros(right_img.shape, np.uint8)
M_right=M_right.astype(int)

OcclusionCost = 20 #(You can adjust this, depending on how much threshold you want to give for noise)

#For Dynamic Programming you have build a cost matrix. Its dimension will be numcols x numcols

N = left_img.shape[0];
M = left_img.shape[1];
#
#n = right_img.shape[0];
#m = right_img.shape[1];

print(left_img)
print(right_img)

print(N,M) 

for X in range (0,N):
    CostMatrix = np.zeros((M,M));
    DirectionMatrix = np.zeros((M,M)); # (This is important in Dynamic Programming. You need to know which direction you need traverse)

##We first populate the first row and column values of Cost Matrix
    
    for i in range(0,M):
        CostMatrix[i][0] = i*OcclusionCost;
        CostMatrix[0][i] = i*OcclusionCost;


    for i in range(0,M):
        for j in range(0,M):
            min1 = CostMatrix[i-1][j-1] + np.absolute(int(left_img[X][i] - right_img[X][j]));         
            min2 = CostMatrix[i-1][j] + OcclusionCost;        
            min3 = CostMatrix[i][j-1] + OcclusionCost;
            cmin = np.min((min1,min2,min3));
            CostMatrix[i][j] = cmin;
            if cmin == min1:
                DirectionMatrix[i][j] = 1;
            if cmin == min2:
                DirectionMatrix[i][j] = 2;
            if cmin == min3:
                DirectionMatrix[i][j] = 3;    
            

                
        p = q = M - 1;
    while((p != 0) and (q != 0)):
        if DirectionMatrix[p][q]==1:
            M_left[X][p]=np.abs(p-q)
            M_right[X][q]=np.abs(p-q)
            p-=1;
            q-=1;
            
        elif DirectionMatrix[p][q]==2:
            p-=1;
            
           
        elif DirectionMatrix[p][q]==3:
            q-=1;
           

    


print("M_Left : ",M_left);
print("M_Right : ",M_right);

  
cv2.imwrite('Left_Disp_image.png',M_left)
cv2.imshow("left image",M_left)
cv2.imwrite('Right_Disp_image.png',M_right)
cv2.imshow("right image",M_right)  


        
    
    

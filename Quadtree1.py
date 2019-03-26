# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:27:47 2019

@author: jatin
"""

import cv2
#import numpy as np
#import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\jatin\OneDrive\Desktop\Project1-images\Project1-images\t1.jpg",0)
img1=cv2.imread(r"C:\Users\jatin\OneDrive\Desktop\Project1-images\Project1-images\t1.jpg",0)
'''Threshold around 10 for Mean absolute error and around 100 for MSE'''
th=10
def Split(img):
    er = 0
    w, h =img.shape
    mu,std = cv2.meanStdDev(img)
    for i in range(w):              #Calculate Mean Absolute Error (MAE)
        for j in range(h):
            er = er + abs(img[i][j]-mu)
    #MAE = er / (w*h)
    MSE=std**2
    if(w >= 2 and h >=2 and th<=MSE):
        Split(img[:int(w/2),:int(h/2)])
        Split(img[int(w/2):int(w),0:int(h/2)])
        Split(img[:int(w/2),int(h/2):int(h)])
        Split(img[int(w/2):int(w),int(h/2):int(h)])
    else:
        finalval(img,w,h,mu)

def finalval(img,w,h,mu):
    for i in range(w):
            for j in range(h):
                img[i][j]=mu
Split(img)
cv2.imshow('Binarizedimage', img)
#cv2.imwrite('t1check.jpg',img1)
#cv2.imwrite('t1quad.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
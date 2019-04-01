# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:27:47 2019

@author: jatin
"""

import cv2
img=cv2.imread(r"Project1-images\t1.jpg",0)
img1=cv2.imread(r"Project1-images\t2.jpg",0)
img2=cv2.imread(r"Project1-images\t3.jpg",0)
th=100    # Threshold around 10 or less for MAE and between 100-200 for MSE     
def Split(img):
    w, h =img.shape
    #mae,mu = MAE(img) # call to MAE 
    mse,mu = MSE(img) # call to MSE
    if(w >= 2 and h >=2 and th<=mse):
        Split(img[:int(w/2),:int(h/2)])
        Split(img[int(w/2):int(w),0:int(h/2)])
        Split(img[:int(w/2),int(h/2):int(h)])
        Split(img[int(w/2):int(w),int(h/2):int(h)])
    else:
        finalval(img,w,h,mu)
def MAE(img):
    er = 0
    w,h = img.shape
    mu,_ = cv2.meanStdDev(img)
    for i in range(w):              
        for j in range(h):
            er = er + abs(img[i][j]-mu) #Calculate Mean Absolute Error (MAE)
    return er/(w*h),mu
def MSE(img):
    er = 0
    w,h = img.shape
    mu, _ = cv2.meanStdDev(img)
    for i in range(w):              
        for j in range(h):
            er = er + (img[i][j]-mu)**2 #Calculate Mean Squared Error (MSE)
    return er/(w*h),mu
    

def finalval(img,w,h,mu):
    for i in range(w):
            for j in range(h):
                img[i][j]=mu
Split(img)
Split(img1)
Split(img2)
cv2.imshow('MSE_t1_th100', img)
cv2.imshow('MSE_t2_th100', img1)
cv2.imshow('MSE_t3_th100', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
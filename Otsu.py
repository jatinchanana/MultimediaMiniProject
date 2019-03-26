# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 01:31:51 2019

@author: jatin
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\jatin\OneDrive\Desktop\Project1-images\Project1-images\t3.jpg",0)
pixel , frequency = np.unique(img,return_counts=True)
plt.bar(pixel,frequency)
w , h = img.shape
size = w * h
Mu = np.zeros(len(pixel))
Pr = frequency/size
Mu = pixel*Pr
def Otsu(Pr,Mu):
    maxvar = 0
    th = 0
    w0 = w1 = 0
    for i in range(256):
        w0 = sum(Pr[0:i+1])
        w1 = sum(Pr[i+1:256])
        if(w0 and w1 !=0):
            var = w0 * w1 *(((sum(Mu[0:i+1])/w0)-(sum(Mu[i+1:256])/w1))**2)
            if(var >= maxvar):
                maxvar = var
                th = i
    return maxvar,th
def Binarize(img,th):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j]<=th):
                img[i][j]=0
            else:
                img[i][j]=255
variance, threshold = Otsu(Pr,Mu)
Binarize(img,threshold)
print(threshold,variance)
cv2.imshow('Binarized image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
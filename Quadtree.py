# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:42:44 2019

@author: jatin
"""

import cv2
import numpy as np
#import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\jatin\OneDrive\Desktop\Project1-images\Project1-images\t1.jpg",0)
img1=cv2.imread(r"C:\Users\jatin\OneDrive\Desktop\Project1-images\Project1-images\t1.jpg",0)
th=100
w,h=img.shape
mu,std=cv2.meanStdDev(img)
def Split(img):
    w, h =img.shape
    mu,std = cv2.meanStdDev(img)
    if(w >= 2 and h >=2):
        """and th<=std**2"""
        Split4(img[:int(w/2),:int(h/2)],img[int(w/2):int(w),0:int(h/2)],img[:int(w/2),int(h/2):int(h)],img[int(w/2):int(w),int(h/2):int(h)])
        """Split(img[:int(w/2),:int(h/2)])
        Split(img[int(w/2):int(w),0:int(h/2)])
        Split(img[:int(w/2),int(h/2):int(h)])
        Split(img[int(w/2):int(w),int(h/2):int(h)])"""
    else:
        finalval(img,w,h,mu)

def finalval(img,w,h,mu):
    for i in range(w):
            for j in range(h):
                img[i][j]=mu
def Split4(img1,img2,img3,img4):
    w1,h1 = img1.shape
    w2,h2 = img2.shape
    w3,h3 = img3.shape
    w4,h4 = img4.shape
    mu1,std1 = cv2.meanStdDev(img1)
    mu2,std2 = cv2.meanStdDev(img2)
    mu3,std3 = cv2.meanStdDev(img3)
    mu4,std4 = cv2.meanStdDev(img4)
    L=[std1**2,std2**2,std3**2,std4**2]
    Emax = np.argmax(L)
    #print(L[Emax])
    if(L[Emax]<=th):
        finalval(img1,w1,h1,mu1)
        finalval(img2,w2,h2,mu2)
        finalval(img3,w3,h3,mu3)
        finalval(img4,w4,h4,mu4)
    elif(L[Emax]>th):
        if(Emax==0):
            #print(img.shape)
            Split(img1)
        elif(Emax==1):
            Split(img2)
        elif(Emax==2):
            Split(img3)
        elif(Emax==3):
            print(img4.shape)
            Split(img4)
    
        
    
Split(img)
#print(img[0:10,0:10])
#print(img1[0:10,0:10])
#cv2.imshow('Binarizedimage', img)
#cv2.imwrite('t2quad.jpg',img)
#cv2.imwrite('t2check.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

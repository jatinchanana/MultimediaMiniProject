# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 01:45:10 2019

@author: jatin
"""
import cv2
import numpy as np
import operator as op
import time
start_time = time.time()
img=cv2.imread(r"C:\Users\jatin\OneDrive\Desktop\Project1-images\Project1-images\t1.jpg")
Box=[]
def GetBins(box,n):
    r=[]
    g=[]
    b=[]
    color=[]
    bin1=[]
    bin2=[]
    for i  in range(box.shape[0]):
        r.append(box[i][0])
        g.append(box[i][1])
        b.append(box[i][2])
        color.append(box[i])
    r1 = (max(r)-min(r))
    r2 = (max(g)-min(g))
    r3 = (max(b)-min(b))
    m = [r1,r2,r3]
    color1=np.asarray(color)
    maxI = m.index(max(m))
    sortcolor=sorted(color1[0:],key=op.itemgetter(maxI))
    sortcolor = np.asarray(sortcolor)
    for i in range(sortcolor.shape[0]):
        if(sortcolor[i][maxI]<=sortcolor[int(sortcolor.shape[0]/2)][maxI]):
            bin1.append(sortcolor[i])
        else:
            bin2.append(sortcolor[i])
    Box.append(np.asarray(bin1))
    Box.append(np.asarray(bin2))
    if(len(Box)<2**n):
        newBin=Box[0]
        Box.pop(0)
        GetBins(newBin,n)    
    
    return Box
def FindMean(Box):
    lm=[]
    for i in range(len(Box)):
        lm.append(np.sum(Box[i],axis = 0)/len(Box[i]))
    return np.asarray(lm)     
def Quantize(img,Bin,listmean):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dist=[]
            for k in range(len(listmean)):
                dist.append(np.linalg.norm(np.asarray(img[i][j])-np.asarray(listmean[k])))
            ind = dist.index(min(dist))
            img[i][j] = listmean[ind]  
    
    return img
             
Bin = GetBins(np.reshape(img,(img.shape[0]*img.shape[1],3)),1)
listmean = FindMean(Bin)
finalimage = Quantize(img,Bin,listmean)
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('Binarized image', finalimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import operator as op
import random
img=cv2.imread(r"Project1-images\t1.jpg")
img1=cv2.imread(r"Project1-images\t1.jpg")
def Random(img,k):  # Randomly select K initial cluster points from the image
    p = []
    img2 = img.reshape(img.shape[0]*img.shape[1],3)
    U_element = np.unique(img2, axis=0)
    rand = random.sample(range(0,len(U_element)),k)
    for i in range(len(rand)):
        p.append(U_element[rand[i]])
    return p
def Clusters(point,img):  # find the Euclidean distance of all the pixels and create a list of clusters
    Box = [[] for i in range(len(point))]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            ls  = []
            for k in range(len(point)):
                ls.append(np.linalg.norm(np.asarray(img[i][j])-np.asarray(point[k])))
            ind = ls.index(min(ls))
            Box[ind].append(img[i][j])
            
    return Box  # List of clusters
def FindMean(Cl):
    lm = np.sum(Cl,axis = 0)/len(Cl)
    return lm
def Kmeans(initial):
    point = initial
    while(True):
        Bin = Clusters(point,img)
        new = []
        dist= []
        for j in range(len(Bin)):
            new.append(FindMean(Bin[j]))
        for k in range(len(Bin)):
            dist.append(abs(point[k][0]-new[k][0])+abs(point[k][1]-new[k][1])+abs(point[k][2]-new[k][2]))
        maxd = max(dist)
        if(maxd<5):
            return new
        else:
            point = new
def Quantize(point,img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dist=[]
            for k in range(len(point)):
                dist.append(np.linalg.norm(np.asarray(img[i][j])-np.asarray(point[k])))
            ind = dist.index(min(dist))
            img[i][j] = point[ind]  
    
    return img
point  = Random(img,2) # No. of clusters
finalpoint = Kmeans(point)
finalimage = Quantize(finalpoint,img1)
cv2.imshow("Final image",finalimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

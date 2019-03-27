import cv2
import numpy as np
import operator as op
import time
start_time = time.time()
img=cv2.imread(r"Project1-images\t1.jpg")
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
    r1 = (max(r)-min(r)) # range of red color
    r2 = (max(g)-min(g)) # range of green color
    r3 = (max(b)-min(b)) # range of blue color
    m = [r1,r2,r3]
    color1=np.asarray(color)
    maxI = m.index(max(m))  # find the color with maximum range
    sortcolor=sorted(color1[0:],key=op.itemgetter(maxI)) # sort the image according to the color 
    sortcolor = np.asarray(sortcolor)
    for i in range(sortcolor.shape[0]):
        if(sortcolor[i][maxI]<=sortcolor[int(sortcolor.shape[0]/2)][maxI]):   # If the color-dimension is lower than the median value 
            bin1.append(sortcolor[i]) # append to bin1 else it goes to bin2 
        else:
            bin2.append(sortcolor[i])
    Box.append(np.asarray(bin1))
    Box.append(np.asarray(bin2))     #Append the bins to the list Box
    if(len(Box)<2**n): # If number of bins is less than 2^n remove the first bin from list and recursively split further 
        newBin=Box[0]
        Box.pop(0)
        GetBins(newBin,n)    
    
    return Box                   # Return the final list of 2^n Bins
def FindMean(Box):
    lm=[]
    for i in range(len(Box)):
        lm.append(np.sum(Box[i],axis = 0)/len(Box[i]))
    return np.asarray(lm)     
def Quantize(img,Bin,listmean):           #Assigns each pixel to a bin based on the Euclidean distance 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dist=[]
            for k in range(len(listmean)):
                dist.append(np.linalg.norm(np.asarray(img[i][j])-np.asarray(listmean[k])))
            ind = dist.index(min(dist))
            img[i][j] = listmean[ind]  
    
    return img
             
Bin = GetBins(np.reshape(img,(img.shape[0]*img.shape[1],3)),1)  #Parameters image and bit depth : 1,2,4 or 8
listmean = FindMean(Bin)
finalimage = Quantize(img,Bin,listmean)
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('Binarized image', finalimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

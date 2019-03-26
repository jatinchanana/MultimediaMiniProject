import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r"t3.jpg",0)
pixel , frequency = np.unique(img,return_counts=True) # Calculates the frequency for each pixel intensity in the image 
plt.bar(pixel,frequency) # Plotting histogram for the intensity values
w , h = img.shape
size = w * h
Mu = np.zeros(len(pixel)) 
Pr = frequency/size  # Probability of each intensity value
Mu = pixel*Pr       # Mean of each pixel intensity 

# OTSU method takes Pr and Mu and finds the threshold with maximum inter-class variance, returns maximum variance and final threshold. 
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
# Binarize takes the image and threshold as parameter and assign all pixels below threshold to 0, 255 otherwise. 
def Binarize(img,th):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j]<=th):
                img[i][j]=0
            else:
                img[i][j]=255
variance, threshold = Otsu(Pr,Mu) # call to OTSU
Binarize(img,threshold) # call to Binarize 
print(threshold,variance)
cv2.imshow('Binarized image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

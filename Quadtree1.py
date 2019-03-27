import cv2
img=cv2.imread(r"Project1-images\t1.jpg",0)
th=100
def Split(img):
    w, h =img.shape
    mu,std = cv2.meanStdDev(img)
    MSE=std**2  # Mean Square error
    MAE = MeanAsoluteError(img)
    if(w >= 2 and h >=2 and th<=MSE):
        Split(img[:int(w/2),:int(h/2)])
        Split(img[int(w/2):int(w),0:int(h/2)])
        Split(img[:int(w/2),int(h/2):int(h)])
        Split(img[int(w/2):int(w),int(h/2):int(h)])
    else:
        finalval(img,w,h,mu)
#Calculate Mean Absolute Error (MAE)
def MeanAbsoluteError(img):
    mu,std = cv2.meanStdDev(img)
    w , h = img.shape
    for i in range(w):              
        for j in range(h):
            er = er + abs(img[i][j]-mu)
    return er/(w*h)
def finalval(img,w,h,mu):
    for i in range(w):
            for j in range(h):
                img[i][j]=mu
Split(img)
cv2.imshow('Binarizedimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

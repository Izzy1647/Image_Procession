import cv2
import numpy as np
path = '/Users/zzy/PycharmProjects/ImageProcession/lena.jpeg'
img = cv2.imread(path)

def GammaTransform(coefficient):
    img2 = np.power(img/float(np.max(img)), coefficient)
    #return img2
    #cv2.imshow('src',img)
    #title = str(coefficient)
    cv2.imshow('GammaWindow',img2)
    cv2.waitKey(0)

cv2.namedWindow('GammaWindow')
cv2.createTrackbar('Gamma','GammaWindow',0,10,GammaTransform)
cv2.imshow('GammaWindow',img)
cv2.waitKey(0)




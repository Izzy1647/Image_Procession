import cv2 as cv

srcImg = cv.imread("/Users/zzy/PycharmProjects/ImageProcession/lplst.png")

img_blur = cv.blur(srcImg,(3,3)) # 3*3的均值模版
img_lpls = cv.Laplacian(img_blur,cv.CV_16S,ksize = 3)
res1 = cv.convertScaleAbs(img_lpls)

cv.imshow("src",srcImg)
# cv.imshow("blurred",img_blur)
cv.imshow("b>l",res1)

img_l = cv.Laplacian(srcImg,cv.CV_16S,ksize = 3)
imlr = cv.convertScaleAbs(img_l)
res2 = cv.blur(imlr,(3,3))
cv.imshow("l>b",res2)


cv.waitKey(0)



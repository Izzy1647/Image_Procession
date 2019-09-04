import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("lplsimgsrc.png")

# 转化为灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('src',img_gray)
cv2.waitKey(0)
img_laplace = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=3)
# cv2.imshow('laplace',img_laplace)
# cv2.waitKey(0)
#result = cv2.add(img_gray,img_laplace)

plt.subplot(231), plt.imshow(img_gray, "gray"), plt.title("Original")
plt.subplot(234), plt.imshow(img_laplace,  "gray"), plt.title("Laplace")
plt.show()

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
dst = cv2.filter2D(img, -1, kernel=kernel)
cv2.imshow('res',dst)
cv2.waitKey(0)

# result = cv2.add(img_gray,img_laplace)
# cv2.imshow('result',result)
# cv2.waitKey(0)

import cv2
#import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("lena.jpeg", 1)

# 绘制直方图
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("src", img)

#彩色图像均衡化 分解通道 对每一个通道均衡化
(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并每一个通道
result = cv2.merge((bH, gH, rH))
cv2.imshow("result", result)

#
# #灰度图均衡化
# eq = cv2.equalizeHist(img)
# cv2.imshow('image2',eq)
# cv2.waitKey(0)

hist = cv2.calcHist([result], [0], None, [256], [0, 256])
plt.hist(result.ravel(), 256, [0, 256])
plt.show()


#cv2.imwrite('vi2.jpg',eq)      #保存图片在当前目录下

#cv2.waitKey(0)

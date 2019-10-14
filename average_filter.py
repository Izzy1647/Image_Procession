import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img1 = cv2.imread('/Users/zzy/PycharmProjects/ImageProcession/DIP3E_Problem_Figures/CH03_Problem_Figures/FigP0314(a).tif')
source1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
result1 = cv2.blur(source1, (5, 5))
cv2.imshow("blurred_1",result1)
# cv2.waitKey(0)
hist1 = cv2.calcHist([result1], [0], None, [256], [0, 256])
plt.hist(result1.ravel(), 256, [0, 256])
plt.show()


img2 = cv2.imread('/Users/zzy/PycharmProjects/ImageProcession/DIP3E_Problem_Figures/CH03_Problem_Figures/FigP0314(b).tif')
source2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
result2 = cv2.blur(source2, (5, 5))
hist2 = cv2.calcHist([result2], [0], None, [256], [0, 256])
plt.hist(result2.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("blurred_2",result2)
cv2.waitKey(0)





# # 显示图形
# titles = ['Source Image', 'Blur Image']
# images = [source, result]
# for i in range(2):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
#
# plt.show()

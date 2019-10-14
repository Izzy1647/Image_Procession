import cv2
import os


#gtding@t.shu.edu.cn

img = cv2.imread('lena.jpeg',-1)
print("img:",img)


height, width = img.shape[:2]
print("h&w:",height,width)

# 缩小图像
size = (int(width * 0.3), int(height * 0.5))
shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)


# 放大图像
fx = 1.6
fy = 1.2
enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)

# 显示
# cv2.imshow("src", img)
# cv2.imshow("shrink", shrink)
# cv2.imshow("enlarge", enlarge)
#
# cv2.waitKey(0)


#放大缩小指定倍数
def resize(img):
    x = float(input("Input the integer:"))
    if(x>=1):
        fx = fy = x
        result_img = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    elif(0<x<1):
        size = (int(width * x), int(height * x))
        result_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    elif(x<0):
        print("error")
        os._exit(0)

    cv2.imshow("res",result_img)
    cv2.imshow("origin",img)
    cv2.waitKey(0)

resize(img)
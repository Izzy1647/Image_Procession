import cv2 as cv




#print(len(new_frame))

def find_median():
    pass




def access_pixels(frame):  # 操作图像的像素

    print(frame.shape)  # 高宽通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]

    # 新图片的矩阵
    new_frame = [[0 for t in range(3)] for i in range(height*weight*channels)]
    print(len(new_frame))  #7500000

    print("weight : %s, height : %s, channel : %s" % (weight, height, channels))

    pvList = []

    for row in range(height):  # 遍历高
        for col in range(weight):  # 遍历宽
            for c in range(channels):  # 遍历通道
                pv = frame[row, col, c]
                pvList.append(pv) # 计算像素总个数





                frame[row, col, c] = 255 - pv  # 全部像素取反，实现一个反向效果
    cv.imshow("fanxiang", frame)

    print(len(pvList))





image = 'lena.jpeg'
src = cv.imread(image)
cv.imshow("Picture", src)
access_pixels(src)
cv.waitKey(0)
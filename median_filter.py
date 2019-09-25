import cv2 as cv
import numpy as np



#print(len(new_frame))

def find_median(list):
    list.sort()
    l = len(list)
    median = -1
    if l%2 != 0:
        median = list[int((l - 1) / 2)]
    elif l%2 == 0:
        median = (list[int(l / 2)] + list[int((l / 2) - 1)]) / 2
    return median



def access_pixels(frame):  # 操作图像的像素

    print(frame.shape)  # 高宽通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]
    # print(frame)

    # 新图片的矩阵
    # new_frame = [[0 for t in range(3)] for i in range(height*weight*channels)]

    new_frame = np.zeros((channels, weight, height), dtype=np.int)
    print(len(new_frame))  #7500000

    print("weight : %s, height : %s, channel : %s" % (weight, height, channels))

    pvList = []

    for row in range(height):  # 遍历高
        for col in range(weight):  # 遍历宽
            for c in range(channels):  # 遍历通道
                pv = frame[row, col, c]
                pvList.append(pv) # 计算像素总个数

                if row>0 & row<499 & col>0 & col<499:
                    nlist = []
                    nlist.extend([frame[row-1,col-1,c],frame[row-1,col,c],frame[row-1,col+1,c],
                                  frame[row,col-1,c],frame[row,col+1,c],frame[row+1,col-1,c],
                                  frame[row+1,col,c],frame[row+1,col+1,c]])
                    resPv = find_median(nlist)
                    print(resPv)
                    new_frame[row,col,c] = resPv

                else:
                    new_frame[row,col,c] = frame[row,col,c]

                # frame[row, col, c] = 255 - pv  # 全部像素取反，实现一个反向效果
    print(len(resPv))
    cv.imshow("median_filtered", new_frame)
    #
    # print(len(pvList))
    # print(frame[499,499,1])

image = 'lena.jpeg'
src = cv.imread(image)
cv.imshow("Picture", src)
access_pixels(src)
cv.waitKey(0)
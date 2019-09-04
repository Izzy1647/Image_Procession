import cv2 as cv
def ReadAndShowImage(path):
    image = cv.imread(path)
    cv.namedWindow('Image',cv.WINDOW_NORMAL)
    cv.imshow('image',image)
    cv.waitKey(0)

ReadAndShowImage('/Users/zzy/PycharmProjects/ImageProcession/test1.png')

import cv2 as cv
capture = cv.VideoCapture(0) #创建videocapture对象
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(2) == ord('q'):
        break

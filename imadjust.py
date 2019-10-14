# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:54:26 2019

@author: ChengGD
"""

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

# from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


import scipy
# import cv2

def imadjust(img, low_in, high_in, low_out, high_out, gamma, c):
    f = misc.imread(img).astype(np.int16)
    plt.figure(1)
    plt.imshow(f, cmap='gray')
    plt.axis('off')
    plt.title('原始图像')
    plt.show()

    w, h = f.shape
    f1 = np.zeros([w, h])
    # imadjust函数运算部分
    for x in range(0, w):
        for y in range(0, h):
            if f[x, y] <= low_in:
                f1[x, y] = low_out
            elif f[x, y] >= high_in:
                f1[x, y] = high_out
            else:
                f1[x, y] = c * (f[x, y] ** gamma)

    scipy.misc.imsave('figure2.png', f1)
    plt.figure(2)
    plt.imshow(f1, cmap='gray')
    plt.axis('off')
    plt.title('变换图像')
    plt.show()

    plt.figure(3)
    f2 = np.abs(f - f1)  # 差值的绝对值

    scipy.misc.imsave('figure3.png', f2)
    plt.imshow(f2, cmap='gray')
    plt.axis('off')
    plt.title('差值图像')
    plt.show()


imadjust('lena.jpeg', 50, 100, 5, 10, 1, 1)

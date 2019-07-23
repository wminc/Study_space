# -*- coding:utf8 -*-
"""
Created on 2019/7/23 13:51

@author: WMaker
"""
'''
如果这两种边界你都想检测到，最好的的办法就是将输出的数据类型
设置的更高，比如 cv2.CV_16S，cv2.CV_64F 等。取绝对值然后再把它转回
到 cv2.CV_8U
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


# 生成3通道的白块的图
box = np.zeros((100,100,3),dtype=np.uint8)

box[30:70,40:60]=255

# cv2.imshow('box',box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

sobel_x_8u = cv2.Sobel(box,cv2.CV_8U,1,0,ksize=5)

sobel_x_64f = cv2.Sobel(box,cv2.CV_64F,1,0,ksize=5)
abs_sobel_64f = np.absolute(sobel_x_64f)
sobel_8u = np.uint8(abs_sobel_64f)

plt.subplot(2, 3, 1), plt.imshow(box), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2), plt.imshow(sobel_x_8u), plt.title('sobel_x_8u')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3), plt.imshow(sobel_x_64f), plt.title('sobel_x_64f')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 4), plt.imshow(abs_sobel_64f), plt.title('abs_sobel_64f')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 5), plt.imshow(sobel_8u), plt.title('sobel_8u')
plt.xticks([]), plt.yticks([])
plt.show()

# img = cv2.imread()
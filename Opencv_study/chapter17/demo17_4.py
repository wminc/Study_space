# -*- coding:utf8 -*-
"""
Created on 2019/7/19 17:05

@author: WMaker
"""

'''
形态学梯度
其实就是一幅图像膨胀与腐蚀的差别。
结果看上去就像前景物体的轮廓。

op = cv2.GRADIENT 用于梯度运算-膨胀图像-腐蚀后的图像

梯度运算：表示的是将膨胀以后的图像 - 腐蚀后的图像，获得了最终的边缘轮廓
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/j.png')
kernel = np.ones((5,5),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

erosion = cv2.erode(img,kernel,iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.show()
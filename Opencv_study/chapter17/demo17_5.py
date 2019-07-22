# -*- coding:utf8 -*-
"""
Created on 2019/7/22 16:43

@author: WMaker
"""

'''
17.6 顶帽
原始图像与进行开运算之后得到的图像的差。

17.7 黑帽
进行闭运算之后得到的图像与原始图像的差

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/j.png')

kernel = np.ones((7,7),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


plt.subplot(131),plt.imshow(img),plt.title('img1_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(tophat),plt.title('img_MORPH_TOPHAT')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blackhat),plt.title('img_MORPH_BLACKHAT')
plt.xticks([]), plt.yticks([])

plt.show()
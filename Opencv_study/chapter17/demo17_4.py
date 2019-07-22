# -*- coding:utf8 -*-
"""
Created on 2019/7/19 17:05

@author: WMaker
"""

'''
17.5 形态学梯度
其实就是一幅图像膨胀与腐蚀的差别。结果看上去就像前景物体的轮廓。

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/j.png')

kernel = np.ones((5,5),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

morph_gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

plt.subplot(121),plt.imshow(img),plt.title('img1_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(morph_gradient),plt.title('img_MORPH_GRADIENT')
plt.xticks([]), plt.yticks([])



plt.show()

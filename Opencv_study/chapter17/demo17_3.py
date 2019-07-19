# -*- coding:utf8 -*-
"""
Created on 2019/7/19 16:53

@author: WMaker
"""
'''
17.3 开运算
先进性腐蚀再进行膨胀就叫做开运算。就像我们上面介绍的那样，它被用
来去除噪声。这里我们用到的函数是 cv2.morphologyEx()。

17.4 闭运算
先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点

17.5 形态学梯度
其实就是一幅图像膨胀与腐蚀的差别。结果看上去就像前景物体的轮廓。

17.6 礼帽
原始图像与进行开运算之后得到的图像的差。

17.7 黑帽
进行闭运算之后得到的图像与原始图像的差


开运算：表示的是先进行腐蚀，再进行膨胀操作

闭运算：表示先进行膨胀操作，再进行腐蚀操作

梯度运算：表示的是将膨胀以后的图像 - 腐蚀后的图像，获得了最终的边缘轮廓


cv2.morphologyEx(src, op, kernel) 进行各类形态学的变化

参数说明:src传入的图片，op进行变化的方式， kernel表示方框的大小

op =  cv2.MORPH_OPEN 进行开运算，指的是先进行腐蚀操作，再进行膨胀操作

op = cv2.MORPH_CLOSE 进行闭运算， 指的是先进行膨胀操作，再进行腐蚀操作

op = cv2.MORPH_GRADIENT 用于梯度运算-膨胀图像-腐蚀后的图像

op = cv2.MORPH_TOPHAT 原始图片-开运算后的图片
闭运算后的图片-原始图片





'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/j.png')
img1 = cv2.imread('../images/j1.png')
img2 = cv2.imread('../images/j2.png')

kernel = np.ones((5,5),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]
img1 = img1[:,:,[2,1,0]]
img2 = img2[:,:,[2,1,0]]

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
morph_gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
hough_gradient = cv2.morphologyEx(img,cv2.HOUGH_GRADIENT,kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(521),plt.imshow(img1),plt.title('img1_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(522),plt.imshow(opening),plt.title('img1_opening')
plt.xticks([]), plt.yticks([])

plt.subplot(523),plt.imshow(img2),plt.title('img2_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(524),plt.imshow(closing),plt.title('img2_closing')
plt.xticks([]), plt.yticks([])

plt.subplot(525),plt.imshow(img),plt.title('img_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(526),plt.imshow(morph_gradient),plt.title('img_MORPH_GRADIENT')
plt.xticks([]), plt.yticks([])

plt.subplot(527),plt.imshow(img),plt.title('img_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(528),plt.imshow(hough_gradient),plt.title('img_HOUGH_GRADIENT')
plt.xticks([]), plt.yticks([])

plt.subplot(529),plt.imshow(tophat),plt.title('img_MORPH_TOPHAT')
plt.xticks([]), plt.yticks([])
plt.subplot(52),plt.imshow(blackhat),plt.title('img_MORPH_BLACKHAT')
plt.xticks([]), plt.yticks([])

plt.show()
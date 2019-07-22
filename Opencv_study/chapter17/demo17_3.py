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


cv2.morphologyEx(src, op, kernel) 进行各类形态学的变化

参数说明
    src：输入图像，可以是灰度图像，可以是彩色图像。

    dst：输出图像。
    
    op：形态学处理的类型
    
    kernel：用于腐蚀运算的核结构元素，可以使用getStructuringElement()函数创建。
    
    anchor：锚点，默认为(-1, -1)
    
    iterations：迭代次数
    
    borderType：边界填充类型
    
    borderValue：边界填充值


op = cv2.MORPH_OPEN 进行开运算，指的是先进行腐蚀操作，再进行膨胀操作

op = cv2.MORPH_CLOSE 进行闭运算， 指的是先进行膨胀操作，再进行腐蚀操作

op = cv2.MORPH_GRADIENT 用于梯度运算-膨胀图像-腐蚀后的图像

op = cv2.MORPH_TOPHAT 原始图片-开运算后的图片

op = cv2.MORPH_BLACKHAT  闭运算后的图片-原始图片





'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/j1.png')
img2 = cv2.imread('../images/j2.png')

kernel = np.ones((5,5),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img1 = img1[:,:,[2,1,0]]
img2 = img2[:,:,[2,1,0]]

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

plt.subplot(221),plt.imshow(img1),plt.title('img1_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(opening),plt.title('img1_opening')
plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(img2),plt.title('img2_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(closing),plt.title('img2_closing')
plt.xticks([]), plt.yticks([])





plt.show()
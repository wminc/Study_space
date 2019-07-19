# -*- coding:utf8 -*-
"""
Created on 2019/7/11 16:34

@author: WMaker
"""

'''
16 图像平滑
目标
• 学习使用不同的低通滤波器对图像进行模糊
• 使用自定义的滤波器对图像进行卷积（2D 卷积）


2D 卷积
我们可以对 2D 图像实施低通滤波（LPF），高通滤波（HPF）等。
LPF 帮助我们去除噪音，模糊图像。HPF 帮助我们找到图像的边缘
OpenCV 提供的函数 cv.filter2D() 可以让我们对一幅图像进行卷积操作。
下面我们将对一幅图像使用平均滤波器。下面是一个 5x5 的平均滤波器核：

           1 1 1 1 1
           1 1 1 1 1
K = (1/25) 1 1 1 1 1   
           1 1 1 1 1
           1 1 1 1 1

操作如下：将核放在图像的一个像素 A 上，求与核对应的图像上 25（5x5）
个像素的和，在取平均数，用这个平均数替代像素 A 的值。重复以上操作直到
将图像的每一个像素值都更新一边。
'''



import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../images/meixi.jpg')

# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

kernel = np.ones((5,5),np.float32)/25

#cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
#ddepth –desired depth of the destination image;
#if it is negative, it will be the same as src.depth();
#the following combinations of src.depth() and ddepth are supported:
#src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
#src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
#src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
#src.depth() = CV_64F, ddepth = -1/CV_64F
#when ddepth=-1, the output image will have the same depth as the source.

dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

'''
图像模糊（图像平滑）
使用低通滤波器可以达到图像模糊的目的。这对与去除噪音很有帮助。其
实就是去除图像中的高频成分（比如：噪音，边界）。所以边界也会被模糊一
点。（当然，也有一些模糊技术不会模糊掉边界）。OpenCV 提供了四种模糊技
术。
'''



# -*- coding:utf8 -*-
"""
Created on 2019/7/19 16:50

@author: WMaker
"""

'''
17.2 膨胀
与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是 1，中心元
素的像素值就是 1。所以这个操作会增加图像中的白色区域（前景）。一般在去
噪声时先用腐蚀再用膨胀。因为腐蚀在去掉白噪声的同时，也会使前景对象变
小。所以我们再对他进行膨胀。这时噪声已经被去除了，不会再回来了，但是
前景还在并会增加。膨胀也可以用来连接两个分开的物体

cv2.dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)

参数说明:

    src：输入图像，可以是灰度图像，可以是彩色图像。
    
    dst：输出图像。
    
    kernel：用于腐蚀运算的核结构元素，可以使用getStructuringElement()函数创建。
    
    anchor：锚点，默认为(-1, -1)
    
    iterations：迭代次数
    
    borderType：边界填充类型
    
    borderValue：边界填充值
膨胀操作原理：存在一个kernel，在图像上进行从左到右，从上到下的平移，如果方框中存在白色，那么这个方框内所有的颜色都是白色
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/j.png')
kernel = np.ones((5,5),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

dilation = cv2.dilate(img,kernel,iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.show()
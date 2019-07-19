# -*- coding:utf8 -*-
"""
Created on 2019/7/11 14:11

@author: WMaker
"""

'''
15.2 自适应阈值
在前面的部分我们使用是全局阈值，整幅图像采用同一个数作为阈值。当
时这种方法并不适应与所有情况，尤其是当同一幅图像上的不同部分的具有不
同亮度时。这种情况下我们需要采用自适应阈值。此时的阈值是根据图像上的
每一个小区域计算与其对应的阈值。因此在同一幅图像上的不同区域采用的是
不同的阈值，从而使我们能在亮度不同的情况下得到更好的结果。
这种方法需要我们指定三个参数，返回值只有一个。
• Adaptive Method- 指定计算阈值的方法。
– cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平
均值
– cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取值相邻区域
的加权和，权重为一个高斯窗口。

cv2.adaptiveThreshold(src, maxval, thresh_type, type, Block Size, C)
src： 输入图，只能输入单通道图像，通常来说为灰度图
dst： 输出图
maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
thresh_type： 阈值的计算方法，包含以下2种类型：cv2.ADAPTIVE_THRESH_MEAN_C； cv2.ADAPTIVE_THRESH_GAUSSIAN_C.
type：二值化操作的类型，与固定阈值函数相同，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV.
Block Size： 图片中分块的大小
C ：阈值计算方法中的常数项
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/meixi.jpg',0)
# 中值滤波
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,190,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 190)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# -*- coding:utf8 -*-
"""
Created on 2019/7/23 9:12

@author: WMaker
"""

'''
18.2 Laplacian 算子
拉普拉斯算子可以使用二阶导数的形式定义，可假设其离散实现类似于二
阶 Sobel 导数，事实上，OpenCV 在计算拉普拉斯算子时直接调用 Sobel 算子。
拉普拉斯滤波器使用的卷积核：
          0 1 0
kernel =  1 4 1
          0 1 0

Laplacian(src, ddepth, dst=None, ksize=None, scale=None, delta=None, borderType=None)
功能：使用Laplacian算子对图像进行处理。
参数：
    src：输入图像。
    dst：输出图像。
    ddepth：输出图像的深度。
    dx：给1，x方向进行计算
    dy：给1，y方向进行计算
    ksize：Sobel算子的大小
    scale：缩放因子
    delta：将处理的图像加上delta
    borderType：边界填充类型
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/shudu.jpg',0)

# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致 np.uint8
# laplacian = cv2.Laplacian(img, -1)
laplacian = cv2.Laplacian(img, cv2.CV_64F)


plt.subplot(1, 2, 1), plt.imshow(img,cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(laplacian,cmap='gray'), plt.title('Laplacian')
plt.xticks([]), plt.yticks([])

plt.show()

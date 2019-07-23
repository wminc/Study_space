# -*- coding:utf8 -*-
"""
Created on 2019/7/22 17:27

@author: WMaker
"""

'''
18.1 Sobel 算子和 Scharr 算子
Sobel 算子是高斯平滑与微分操作的结合体，所以它的抗噪声能力很好。
你可以设定求导的方向（xorder 或 yorder）。还可以设定使用的卷积核的大
小（ksize）。如果 ksize=-1，会使用 3x3 的 Scharr 滤波器，它的的效果要
比 3x3 的 Sobel 滤波器好（而且速度相同，所以在使用 3x3 滤波器时应该尽
量使用 Scharr 滤波器）。3x3 的 Scharr 滤波器卷积核如下：
         -3  0  3
x方向    -10  0 10
         -3  0  3 

        -3 -10 -3
y 方向   0  0   0 
         3  10  3

Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)     
功能：使用Sobel算子对图像进行处理。
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

Scharr(src, ddepth, dx, dy, dst=None, scale=None, delta=None, borderType=None)
功能：使用Scharr算子对图像进行处理。
参数：
    src：输入图像。
    dst：输出图像。
    ddepth：输出图像的深度。
    dx：给1，x方向进行计算
    dy：给1，y方向进行计算
    scale：缩放因子
    delta：将处理的图像加上delta
    borderType：边界填充类型
         
'''

import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('../images/shudu.jpg')
# img = img[:,:,[2,1,0]]

img = cv2.imread('../images/shudu.jpg', 0)

# 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)

scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)

plt.subplot(2, 2, 1), plt.imshow(sobel_x, cmap='gray'), plt.title('Sobel X')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(sobel_y, cmap='gray'), plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(scharr_x, cmap='gray'), plt.title('Scharr X')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(scharr_y, cmap='gray'), plt.title('Scharr Y')
plt.xticks([]), plt.yticks([])
plt.show()

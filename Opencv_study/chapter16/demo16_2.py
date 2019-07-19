# -*- coding:utf8 -*-
"""
Created on 2019/7/11 16:57

@author: WMaker
"""

'''
16.2 高斯模糊
现在把卷积核换成高斯核（简单来说，方框不变，将原来每个方框的值是
相等的，现在里面的值是符合高斯分布的，方框中心的值最大，其余方框根据
距离中心元素的距离递减，构成一个高斯小山包。原来的求平均数现在变成求
加权平均数，全就是方框里的值）。实现的函数是 cv2.GaussianBlur()。我
们需要指定高斯核的宽和高（必须是奇数）。以及高斯函数沿 X，Y 方向的标准
差。如果我们只指定了 X 方向的的标准差，Y 方向也会取相同值。如果两个标
准差都是 0，那么函数会根据核函数的大小自己计算。高斯滤波可以有效的从
图像中去除高斯噪音。
如果你愿意的话，你也可以使用函数 cv2.getGaussianKernel() 自己
构建一个高斯核。


cv2.Guassianblur(img, (3, 3), 1) 表示进行高斯滤波， 

参数说明: 1表示σ， x表示与当前值得距离，计算出的G(x)表示权重值
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/Ball.png')
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
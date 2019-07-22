# -*- coding:utf8 -*-
"""
Created on 2019/7/22 17:12

@author: WMaker
"""

'''
结构化元素
在前面的例子中我们使用 Numpy 构建了结构化元素，它是正方形的。但
有时我们需要构建一个椭圆形/圆形的核。

为了实现这种要求，提供了 OpenCV函数
getStructuringElement(shape, ksize, anchor=None)

功能：返回指定大小和形状的结构元素，用于形态学处理。

参数：

shape：元素形状。

ksize：大小

anchor：锚点，默认为(-1, -1)

shape的取值如下：

cv2.MORPH_RECT：矩形结构元素

cv2.MORPH_CROSS：十字形结构元素

cv2.MORPH_ELLIPSE：椭圆形结构元素
'''

import cv2

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

print(kernel_rect)

kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

print(kernel_cross)

kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

print(kernel_ellipse)
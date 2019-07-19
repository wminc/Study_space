# -*- coding:utf8 -*-
"""
Created on 2019/7/11 13:51

@author: WMaker
"""

'''
15 图像阈值
目标
• 本节你将学到简单阈值，自适应阈值，Otsu’s 二值化等
• 将要学习的函数有 cv2.threshold，cv2.adaptiveThreshold 等。
15.1 简单阈值
与名字一样，这种方法非常简单。但像素值高于阈值时，我们给这个像素
赋予一个新值（可能是白色），否则我们给它赋予另外一种颜色（也许是黑色）。
这个函数就是 cv2.threshhold()。这个函数的第一个参数就是原图像，原图
像应该是灰度图。第二个参数就是用来对像素值进行分类的阈值。第三个参数
就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值。OpenCV
提供了多种不同的阈值方法，这是有第四个参数来决定的。这些方法包括：
• cv2.THRESH_BINARY
• cv2.THRESH_BINARY_INV
• cv2.THRESH_TRUNC
• cv2.THRESH_TOZERO
• cv2.THRESH_TOZERO_INV
上图摘选自《学习 OpenCV》中文版，其实这些在文档中都有详细介绍了，
你也可以直接查看文档。
这个函数有两个返回值，第一个为 retVal，我们后面会解释。第二个就是
阈值化之后的结果图像了。
'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/meixi.jpg',0)
# cv2读取出来的是bgr,图像处理时先转为rgb,灰度图，不用转

ret,thresh1 = cv2.threshold(img,190,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,190,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,190,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,190,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,190,255,cv2.THRESH_TOZERO_INV)

titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
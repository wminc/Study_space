# -*- coding:utf8 -*-
"""
Created on 2019/7/11 9:54

@author: WMaker
"""

'''
几何变换
目标
• 学习对图像进行各种几个变换，例如移动，旋转，仿射变换等。
• 将要学到的函数有：cv2.getPerspectiveTransform。
变换
OpenCV 提供了两个变换函数，cv2.warpAffine 和 cv2.warpPerspective，
使用这两个函数你可以实现所有类型的变换。cv2.warpAffine 接收的参数是
2 × 3 的变换矩阵，而 cv2.warpPerspective 接收的参数是 3 × 3 的变换矩
阵。


14.1 扩展缩放
扩展缩放只是改变图像的尺寸大小。OpenCV 提供的函数 cv2.resize()
可以实现这个功能。图像的尺寸可以自己手动设置，你也可以指定缩放因子。我
们可以选择使用不同的插值方法。在缩放时我们推荐使用 cv2.INTER_AREA，
在扩展时我们推荐使用 v2.INTER_CUBIC（慢) 和 v2.INTER_LINEAR。
默认情况下所有改变图像尺寸大小的操作使用的插值方法都是 cv2.INTER_LINEAR。
你可以使用下面任意一种方法改变图像的尺寸：

def resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
'''


import cv2
import numpy as np

img = cv2.imread('../images/meixi.jpg')
# 下面的 None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子fx,fy
# fx 是对图片的宽，fy是对图片的高
# 因此这里为 None
res1 = cv2.resize(img,None,fx=0.5,fy=2,interpolation=cv2.INTER_CUBIC)


# res1 = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height,width=img.shape[:2]
res2 = cv2.resize(img,(width//2,height//2),interpolation=cv2.INTER_CUBIC)

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
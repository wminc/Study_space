# -*- coding:utf8 -*-
"""
Created on 2019/7/12 15:14

@author: WMaker
"""

'''
通过滑动滚动条来展示，对Canny()的效果
'''

import cv2
import numpy as np


# 定义滑动条回调函数，此处pass用作占位语句保持程序结构的完整性
def nothing(x):
    pass


# 窗口名称
winName = 'Canny thresh'

# 原始图片
img_original = cv2.imread('../images/meixi.jpg',0)

# 新建窗口
cv2.namedWindow(winName)

cv2.createTrackbar('thresh-min', winName, 0, 255, nothing)
cv2.createTrackbar('thresh-max', winName, 0, 255, nothing)

while (1):
    # 函数cv2.getTrackbarPos()范围当前滑块对应的值
    minval = cv2.getTrackbarPos('thresh-min', winName)
    maxval = cv2.getTrackbarPos('thresh-max', winName)

    # 输入图像与输入图像在掩模条件下按位与，得到掩模范围内的原图像
    edges = cv2.Canny(img_original,minval,maxval)

    cv2.imshow(winName, edges)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

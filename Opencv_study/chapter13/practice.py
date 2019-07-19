# -*- coding:utf8 -*-
"""
Created on 2019/7/12 15:14

@author: WMaker
"""

'''
通过滑动滚动条来展示，对转成HSV格式的图片中提取指定颜色
'''

import cv2
import numpy as np


# 定义滑动条回调函数，此处pass用作占位语句保持程序结构的完整性
def nothing(x):
    pass


# 窗口名称
winName = 'HSV Image get color region'

# 原始图片
img_original = cv2.imread('../images/color.jpg')
# 颜色空间的转换
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

# 新建窗口
cv2.namedWindow('HSV Image get color region')

# 新建6个滑动条，表示颜色范围的上下边界，这里滑动条的初始化位置即为黄色的颜色范围
cv2.createTrackbar('B-low', winName, 0, 255, nothing)
cv2.createTrackbar('G-low', winName, 0, 255, nothing)
cv2.createTrackbar('R-low', winName, 0, 255, nothing)
cv2.createTrackbar('B-upper', winName, 0, 255, nothing)
cv2.createTrackbar('G-upper', winName, 0, 255, nothing)
cv2.createTrackbar('R-upper', winName, 0, 255, nothing)

while (1):
    # 函数cv2.getTrackbarPos()范围当前滑块对应的值
    B_low = cv2.getTrackbarPos('B-low', winName)
    G_low = cv2.getTrackbarPos('G-low', winName)
    R_low = cv2.getTrackbarPos('R-low', winName)
    B_upper = cv2.getTrackbarPos('B-upper', winName)
    G_upper = cv2.getTrackbarPos('G-upper', winName)
    R_upper = cv2.getTrackbarPos('R-upper', winName)

    lower = np.array([B_low, G_low, R_low])
    upper = np.array([B_upper, G_upper, R_upper])
    # 对hsv图取掩模
    img_mask = cv2.inRange(img_hsv, lower, upper)

    # 输入图像与输入图像在掩模条件下按位与，得到掩模范围内的原图像
    img_specifiedColor = cv2.bitwise_and(img_original, img_original, mask=img_mask)
    cv2.imshow(winName, img_specifiedColor)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

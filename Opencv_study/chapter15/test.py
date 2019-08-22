# -*- coding:utf8 -*-
"""
Created on 2019/7/11 14:35

@author: WMaker
"""

import cv2
import numpy as np

# 拓展，使用滑动条控制阈值，类型，最大值来展现图片处理效果

def nothing(x):
    pass

# THRESH_BINARY=0,
# THRESH_BINARY_INV=1,
# THRESH_TRUNC=2,
# THRESH_TOZERO=3,
# THRESH_TOZERO_INV=4

gray_img = cv2.imread('../images/cpw.jpg',0)

cv2.namedWindow('test_window')

cv2.createTrackbar('thresh_type','test_window',0,4,nothing)
cv2.createTrackbar('thresh','test_window',0,255,nothing)
cv2.createTrackbar('maxval','test_window',0,255,nothing)
switch='OFF/ON(0/1)'
cv2.createTrackbar(switch,'test_window',0,1,nothing)

while(1):

    type_num = cv2.getTrackbarPos('thresh_type', 'test_window')
    thresh_val = cv2.getTrackbarPos('thresh', 'test_window')
    maxval = cv2.getTrackbarPos('maxval', 'test_window')
    ret, img = cv2.threshold(gray_img, thresh_val, maxval, type_num)
    s = cv2.getTrackbarPos(switch, 'test_window')
    if s == 0:
        img = gray_img
    cv2.imshow('test_window', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        #按下ESC退出
        break

cv2.destroyAllWindows()

# -*- coding:utf8 -*-
# author = 'WMaker'

'''
图像 ROI (region of interest)
有时你需要对一幅图像的特定区域进行操作。例如我们要检测一副图像中
眼睛的位置，我们首先应该在图像中找到脸，再在脸的区域中找眼睛，而不是
直接在一幅图像中搜索。这样会提高程序的准确性和性能。
ROI 也是使用 Numpy 索引来获得的。现在我们选择球的部分并把他拷贝
到图像的其他区域。
'''

import cv2
import numpy as np
cv2_img=cv2.imread('../images/meixi.jpg')

# [274:320,343:390] ----> [y1:y2,x1:x2] ----->[图像区域高度区间，图像区域宽度区间]
# 以图片左上角为(0,0),向右为x轴正方向，向下为y轴正方向
# y1指复制的图像区域 起始纵坐标，y2指复制的图像区域 终点纵坐标，x1指复制的图像区域 起始横坐标，x2指复制的图像区域 终点横坐标
# ball = cv2_img[343:390,274:320]
ball = cv2_img[274:320,343:390]
# cv2_img[100:147,200:256] = ball
cv2_img[200:246,100:147] = ball

cv2.imshow('123',cv2_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
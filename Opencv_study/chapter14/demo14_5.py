# -*- coding:utf8 -*-
"""
Created on 2019/7/11 11:31

@author: WMaker
"""

'''
14.5 透视变换
对于视角变换，我们需要一个 3x3 变换矩阵。在变换前后直线还是直线。
要构建这个变换矩阵，你需要在输入图像上找 4 个点，以及他们在输出图
像上对应的位置。这四个点中的任意三个都不能共线。这个变换矩阵可以有
函数 cv2.getPerspectiveTransform() 构建。然后把这个矩阵传给函数
cv2.warpPerspective。
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/bankcard.jpg')
height,width = img.shape[:2]

# pts1 = np.float32([[70,80],[73,430],[295,70],[290,450]])
#
# pts2 = np.float32([[0,0],[0,400],[300,0],[300,400]])

# 以图片左上角为坐标原点，向下为y轴正向，向右为x轴正向
# 四个坐标[[x1，y1],[x2，y2],[x3，y3],[x4，y4]]
pts1 = np.float32([[80,70],[430,73],[70,295],[450,290]])

pts2 = np.float32([[0,0],[400,0],[0,300],[400,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

# warpPerspective参数同warpAffine
dst = cv2.warpPerspective(img,M,(400,300))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()

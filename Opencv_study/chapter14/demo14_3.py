# -*- coding:utf8 -*-
"""
Created on 2019/7/11 11:09

@author: WMaker
"""

'''
14.3 旋转
对一个图像旋转角度 θ, 需要使用到下面形式的旋转矩阵。
    cosθ  -sinθ 
M =
    sinθ  cosθ

但是 OpenCV 允许你在任意地方进行旋转，但是旋转矩阵的形式应该修
改为

    α  β  (1-α)·(center x)-β·(center y)
    
    -β α  β·(center x)+(1-α)·(center x)

其中：
α = scale · cos θ 
β = scale · sin θ
为了构建这个旋转矩阵，OpenCV 提供了一个函数：cv2.getRotationMatrix2D。
下面的例子是在不缩放的情况下将图像旋转 90 度。
'''
import cv2
import numpy as np

img = cv2.imread('../images/meixi.jpg',0)
height,width=img.shape[:2]

# 这里的第一个参数为旋转中心坐标，该旋转中心可以是图片的任何位置
# 第二个为旋转角度(逆时针方向)，
# 第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((width/2,height/2),30,1)

dst = cv2.warpAffine(img,M,(width,height))

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding:utf8 -*-
"""
Created on 2019/7/11 10:48

@author: WMaker
"""

'''
平移
平移就是将对象换一个位置。如果你要沿（x，y）方向移动，移动的距离
是（tx，ty），你可以以下面的方式构建移动矩阵：
     0 1 tx
M = 
     1 0 ty 
你可以使用 Numpy 数组构建这个矩阵（数据类型是 np.float32），然
后把它传给函数 cv2.warpAffine()。


src - 输入图像。
M - 变换矩阵。
dsize - 输出图像的大小。
flags - 插值方法的组合（int 类型！）
borderMode - 边界像素模式（int 类型！）
borderValue - （重点！）边界填充值; 默认情况下，它为0。

上述参数中：M作为仿射变换矩阵，一般反映平移或旋转的关系，为InputArray类型的2×3的变换矩阵。

flages表示插值方式，默认为 flags=cv2.INTER_LINEAR，表示线性插值，此外还有：
cv2.INTER_NEAREST（最近邻插值）   
cv2.INTER_AREA （区域插值）  
cv2.INTER_CUBIC（三次样条插值）    
cv2.INTER_LANCZOS4（Lanczos插值）

日常进行仿射变换时，在只设置前三个参数的情况下，如 cv2.warpAffine(img,M,(图片宽,图片高))可以实现基本的仿射变换效果，
但可以出现“黑边”现象

'''

import cv2
import numpy as np


img = cv2.imread('../images/meixi.jpg')
height,width=img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])
res = cv2.warpAffine(img,M,(width,height))

cv2.imshow('img',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()



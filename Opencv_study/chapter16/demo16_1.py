# -*- coding:utf8 -*-
"""
Created on 2019/7/11 16:50

@author: WMaker
"""
'''
16.1 均值模糊
这是由一个归一化卷积框完成的。他只是用卷积框覆盖区域所有像素的平
均值来代替中心元素。可以使用函数 cv2.blur()。我们需要设定卷积框的
宽和高。下面是一个 3x3 的归一化卷积框：
 
          1 1 1
K = (1/9) 1 1 1
          1 1 1

cv2.blur(img, (3, 3))  进行均值滤波
参数说明：img表示输入的图片， (3, 3) 表示进行均值滤波的方框大小

cv2.boxfilter(img, -1, (3, 3), normalize=True) 表示进行方框滤波，
参数说明当normalize=True时，与均值滤波结果相同， normalize=False，表示对加和后的结果不进行平均操作，大于255的使用255表示
'''

#注意：如果你不想使用归一化卷积框，你应该使用 cv2.boxFilter()，这时要传入参数 normalize=False。


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/Ball.png')
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

blur = cv2.blur(img,(3,3))

boxfilter = cv2.boxFilter(img, -1, (3, 3), normalize=True)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(boxfilter),plt.title('boxfilter')
plt.xticks([]), plt.yticks([])
plt.show()
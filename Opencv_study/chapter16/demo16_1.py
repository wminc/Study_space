# -*- coding:utf8 -*-
"""
Created on 2019/7/11 16:50

@author: WMaker
"""
'''
16.1 平均
这是由一个归一化卷积框完成的。他只是用卷积框覆盖区域所有像素的平
均值来代替中心元素。可以使用函数 cv2.blur() 和 cv2.boxFilter() 来完
这个任务。可以同看查看文档了解更多卷积框的细节。我们需要设定卷积框的
宽和高。下面是一个 3x3 的归一化卷积框：
 
          1 1 1
K = (1/9) 1 1 1
          1 1 1

'''

#注意：如果你不想使用归一化卷积框，你应该使用 cv2.boxFilter()，这时要传入参数 normalize=False。


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/Ball.png')
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
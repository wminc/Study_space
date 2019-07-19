# -*- coding:utf8 -*-
"""
Created on 2019/7/11 11:20

@author: WMaker
"""

'''
14.4 仿射变换
在仿射变换中，原图中所有的平行线在结果图像中同样平行。为了创建这
个矩阵我们需要从原图像中找到三个点以及他们在输出图像中的位置。然后
cv2.getAffineTransform 会创建一个 2x3 的矩阵，最后这个矩阵会被传给
函数 cv2.warpAffine。
'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('../images/meixi.jpg')
height,width,ch=img.shape
print(height,width)

pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])

M=cv2.getAffineTransform(pts1,pts2)

dst=cv2.warpAffine(img,M,(width,height))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(121,plt.imshow(img),plt.title('Input'))
# plt.subplot(121,plt.imshow(img),plt.title('Output'))
# plt.show()
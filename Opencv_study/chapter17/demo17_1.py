# -*- coding:utf8 -*-
"""
Created on 2019/7/19 16:30

@author: WMaker
"""

'''
17.1 腐蚀
就像土壤侵蚀一样，这个操作会把前景物体的边界腐蚀掉（但是前景仍然
是白色）。这是怎么做到的呢？卷积核沿着图像滑动，如果与卷积核对应的原图
像的所有像素值都是 1，那么中心元素就保持原来的像素值，否则就变为零。
这回产生什么影响呢？根据卷积核的大小靠近前景的所有像素都会被腐蚀
掉（变为 0），所以前景物体会变小，整幅图像的白色区域会减少。这对于去除
白噪声很有用，也可以用来断开两个连在一块的物体等。


cv2.erode(src, kernel, iteration)

参数说明：src表示的是输入图片，kernel表示的是方框的大小，iteration表示迭代的次数
腐蚀操作原理：存在一个kernel，比如(5, 5)，在图像中不断的平移，在这个25方框中，哪一种颜色所占的比重大，25个方格中将都是这种颜色
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/j.png')
kernel = np.ones((5,5),np.uint8)
# cv2读取出来的是bgr,图像处理时先转为rgb
img = img[:,:,[2,1,0]]

erosion = cv2.erode(img,kernel,iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.show()
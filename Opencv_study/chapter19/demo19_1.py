# -*- coding:utf8 -*-
"""
Created on 2019/7/23 14:24

@author: WMaker
"""

'''
19.2 OpenCV 中的 Canny 边界检测
在 OpenCV 中只需要一个函数：cv2.Canny()，就可以完成以上几步。
让我们看如何使用这个函数。这个函数的第一个参数是输入图像。第二和第三
个分别是 minVal 和 maxVal。第三个参数设置用来计算图像梯度的 Sobel
卷积核的大小，默认值为 3。最后一个参数是 L2gradient，它可以用来设定
求梯度大小的方程。如果设为 True，就会使用我们上面提到过的方程，否则
使用方程：Edgee Gradient(G) = |G2x| + |G2y| 代替，默认值为 False。

Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
功能：使用Canny算子对图像进行处理。

参数：
    src：输入图像。8bit图像
    edges：输出图像。
    threshold1：阈值1
    threshold2：阈值2
    apertureSize：孔径尺寸，默认3
    L2gradient：是否使用L2范数，默认false
'''


import cv2
from matplotlib import pyplot as plt

img_cv2_gray = cv2.imread('../images/meixi.jpg',0)

# img_rgb = img_cv2[:,:,[2,1,0]]

edges = cv2.Canny(img_cv2_gray,100,200)

cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(121),plt.imshow(img_cv2_gray,cmap='gray'),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray'),plt.title('Canny')
plt.xticks([]),plt.yticks([])
plt.show()
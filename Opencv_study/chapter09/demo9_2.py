# -*- coding:utf8 -*-
# author = 'WMaker'

'''
获取图像属性
图像的属性包括：行，列，通道，图像数据类型，像素数目等
'''

import cv2

cv2_img = cv2.imread('../images/slice.jpg')

# img.shape 可以获取图像的形状。他的返回值是一个包含行数，列数，通道数的元组。
print(cv2_img.shape)
print(cv2_img.shape[:2])

# 注意：如果图像是灰度图，返回值仅有行数和列数。所以通过检查这个返回值
# 就可以知道加载的是灰度图还是彩色图。


#img.size 可以返回图像的像素数目
print(cv2_img.size)

#img.dtype 返回的是图像的数据类型.
print(cv2_img.dtype)

#注意：在除虫（debug）时 img.dtype 非常重要。因为在 OpenCV-Python 代码中经常出现数据类型的不一致。
# -*- coding:utf8 -*-
# author = 'WMaker'

'''
图像上的算术运算
目标
• 学习图像上的算术运算，加法，减法，位运算等。
• 我们将要学习的函数与有：cv2.add()，cv2.addWeighted() 等。

图像加法
你可以使用函数 cv2.add() 将两幅图像进行加法运算，当然也可以直接使
用 numpy，res=img1+img。两幅图像的大小，类型必须一致，或者第二个
图像可以使一个简单的标量值。
'''

# 注意：OpenCV 中的加法与 Numpy 的加法是有所不同的。
# OpenCV 的加法是一种饱和操作，而 Numpy 的加法是一种模操作。

import cv2
import numpy as np
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y)) # 250+10 = 260 => 255
#  [[255]]
print(x+y) # 250+10 = 260 % 256 = 4
#  [4]

#这种差别在你对两幅图像进行加法时会更加明显。OpenCV 的结果会更好一点。所以我们尽量使用 OpenCV 中的函数
img1=cv2.imread('../images/meixi.jpg')
img2=cv2.imread('../images/opencv.jpg')
dst1 = cv2.add(img1,img2)
cv2.imshow('dst1',dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()

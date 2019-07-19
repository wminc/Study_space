# -*- coding:utf8 -*-
# author = 'WMaker'


'''
程序性能检测及优化
目标
在图像处理中你每秒钟都要做大量的运算，所以你的程序不仅要能给出正
确的结果，同时还必须要快。所以这节我们将要学习：
• 检测程序的效率
• 一些能够提高程序效率的技巧
• 你要学到的函数有：cv2.getTickCount,cv2.getTickFrequency
等
除了 OpenCV，Python 也提供了一个叫 time 的的模块，你可以用它来测量
程序的运行时间。另外一个叫做 profile 的模块会帮你得到一份关于你的程序
的详细报告，其中包含了代码中每个函数运行需要的时间，以及每个函数被调
用的次数。如果你正在使用 IPython 的话，所有这些特点都被以一种用户友好
的方式整合在一起了。


使用 OpenCV 检测程序效率
cv2.getTickCount 函数返回从参考点到这个函数被执行的时钟数。所
以当你在一个函数执行前后都调用它的话，你就会得到这个函数的执行时间
（时钟数）。
cv2.getTickFrequency 返回时钟频率，或者说每秒钟的时钟数。所以
你可以按照下面的方式得到一个函数运行了多少秒：


调用中值滤波器的方法与调用其他滤波器的方法类似，如下：

cv2.medianBlur(image,5)
函数返回处理结果，第一个参数是待处理图像，第二个参数是孔径的尺寸，一个大于1的奇数。
比如这里是5，中值滤波器就会使用5×5的范围来计算。即对像素的中心值及其5×5邻域组成了一个数值集，对其进行处理计算，当前像素被其中值替换掉。
---------------------
'''

import cv2
import numpy as np

e1 = cv2.getTickCount()
print(e1)
e2 = cv2.getTickCount()
print(e2)
time = (e2 - e1) / cv2.getTickFrequency()
print(time)

print('*' * 30)
img1 = cv2.imread('../images/meixi.jpg')
e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)

# 注 意： 你 也 可 以 time 模 块 中 实 现 上 面 的 功 能。
# 但 是 要 用 的 函 数 是time.time() 而不是 cv2.getTickCount。

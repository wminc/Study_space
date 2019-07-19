# -*- coding:utf8 -*-
# author = 'WMaker'

'''
获取像素值并修改
'''

import cv2
cv2_img = cv2.imread('../images/slice.jpg')

#你可以根据像素的行和列的坐标获取他的像素值。对 BGR 图像而言，返回值为 B，G，R 的值
px = cv2_img[10,10]
print(px)

blue = cv2_img[10,10,0]
green = cv2_img[10,10,1]
red = cv2_img[10,10,2]
print(blue,green,red)

cv2_img[2,2]=[255,255,255]
print(cv2_img[2,2])

print('---------------------------------------')
# 警告：Numpy 是经过优化了的进行快速矩阵运算的软件包。所以我们不推荐
# 逐个获取像素值并修改，这样会很慢，能有矩阵运算就不要用循环。

# 注意：上面提到的方法被用来选取矩阵的一个区域，比如说前 5 行的后 3列。
# 对于获取每一个像素值，也许使用 Numpy 的 array.item() 和 array.itemset() 会更好。
# 但是返回值是标量。如果你想获得所有 B，G，R 的
# 值，你需要使用 array.item() 分割他们。

import cv2
cv2_img =cv2.imread('../images/slice.jpg')
print(cv2_img.item(10,10,2))

cv2_img.itemset((10,10,2),100)

print(cv2_img.item(10,10,2))
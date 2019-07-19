# -*- coding:utf8 -*-
# author = 'WMaker'


'''
按位运算
这里包括的按位操作有：AND，OR，NOT，XOR 等。当我们提取图像的
一部分，选择非矩形 ROI 时这些操作会很有用（下一章你就会明白）。下面的
例子就是教给我们如何改变一幅图的特定区域。
我想把 OpenCV 的标志放到另一幅图像上。如果我使用加法，颜色会改
变，如果使用混合，会得到透明效果，但是我不想要透明。如果他是矩形我可
以象上一章那样使用 ROI。但是他不是矩形。
'''
import cv2
import numpy as np
# 加载图像
img1 = cv2.imread('../images/meixi.jpg')
img2 = cv2.imread('../images/Ball.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
print(img2.shape)

roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image-New1", img2gray)
cv2.waitKey()
# print(img2gray)
# 下面函数将大于180像素的值置为0,小于的置为255
ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY_INV)
# print(ret,mask)

cv2.imshow("mask", mask)
cv2.waitKey()
# Now black-out the area of logo in ROI
# 取 roi 中与 mask 中对应不为零的值对应的像素的值，其他mask 中为零值在roi中也设置为 0 # 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
cv2.imshow("roi_mask", img1_bg)
cv2.waitKey()

mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask_inv", mask_inv)
cv2.waitKey()

# 取img2中与 mask_inv 中不为零的值对应的像素的值，其他mask 中为零值在img2中也设置为 0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
cv2.imshow("img2_maskinv", img2_fg)
cv2.waitKey()
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)

img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
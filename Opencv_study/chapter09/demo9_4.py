# -*- coding:utf8 -*-
# author = 'WMaker'

'''
拆分及合并图像通道
有时我们需要对 BGR 三个通道分别进行操作。这是你就需要把 BGR 拆
分成单个通道。有时你需要把独立通道的图片合并成一个 BGR 图像
'''

import cv2
import numpy as np
img = cv2.imread('../images/meixi.jpg')
# print(img)
# 三维
print(img.shape)

# 注意：cv2.split函数分离得到各个通道的灰度值(单通道图像)。cv2.merge函数是合并单通道成多通道（不能合并多个多通道图像）
B,G,R=cv2.split(img)
# 二维
print(B)
print(B.shape)

# cv2.imshow("Red", R)
# cv2.imshow("Green", G)
# cv2.imshow("Blue", B)
# cv2.waitKey(0)

print('---------------------------------------------')
# 扩展另外两个通道，但另外两个通道值为0, 而得到上面的这样的图像。代码如下：

# 生成一个值为0的单通道数组
zeros = np.zeros(img.shape[:2], dtype="uint8")

# 分别扩展B、G、R成为三通道。另外两个通道用上面的值为0的数组填充
# cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
# cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
# cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
# cv2.waitKey(0)


print('------------------------------')
import cv2
import numpy as np

img=cv2.imread('../images/meixi.jpg')
b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2]
print(b)

#假如你想使所有像素的红色通道值都为 0，你不必先拆分再赋值。
# 你可以直接使用 Numpy 索引，这会更快。
import cv2
import numpy as np
img=cv2.imread('../images/meixi.jpg')
img[:,:,2]=0

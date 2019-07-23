# -*- coding:utf8 -*-
"""
Created on 2019/7/23 15:47

@author: WMaker
"""

'''
20.2 使用金字塔进行图像融合
图像金字塔的一个应用是图像融合。例如，在图像缝合中，你需要将两幅
图叠在一起，但是由于连接区域图像像素的不连续性，整幅图的效果看起来会
很差。这时图像金字塔就可以排上用场了，他可以帮你实现无缝连接。这里的
一个经典案例就是将两个水果融合成一个


你可以通过阅读后边的更多资源来了解更多关于图像融合，拉普拉斯金字塔的细节。
实现上述效果的步骤如下：
1. 读入两幅图像，苹果和橘子
2. 构建苹果和橘子的高斯金字塔（6 层）
3. 根据高斯金字塔计算拉普拉斯金字塔
4. 在拉普拉斯的每一层进行图像融合（苹果的左边与橘子的右边融合）
5. 根据融合后的图像金字塔重建原始图像。
'''

import cv2
import numpy as np,sys

apple = cv2.imread('../images/apple.jpg')
orange = cv2.imread('../images/orange.jpg')


# 获取苹果的高斯金字塔，原图+6个构造的图
A = apple.copy()
gpA = [A]
for i in range(6):
    A = cv2.pyrDown(A)
    gpA.append(A)

print(len(gpA))
# print(gpA)

# 获取橘子的高斯金字塔,原图+6个构造的图
B = orange.copy()
gpB = [B]
for i in range(6):
    B = cv2.pyrDown(B)
    gpB.append(B)

print(len(gpB))
# print(gpB)

# 获取苹果的拉布拉斯金字塔，6个图
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)


# 获取橘子的拉布拉斯金字塔，6个图
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)


LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imshow('Pyramid_blending2.jpg',ls_)
cv2.imshow('Direct_blending.jpg',real)

cv2.waitKey(0)
cv2.destroyAllWindows()
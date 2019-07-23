# -*- coding:utf8 -*-
"""
Created on 2019/7/23 15:19

@author: WMaker
"""

'''
有两类图像金字塔：高斯金字塔和拉普拉斯金字塔。
高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的。顶
部图像中的每个像素值等于下一层图像中 5 个像素的高斯加权平均值。这样
操作一次一个 MxN 的图像就变成了一个 (M/2 x N/2 )的图像。所以这幅图像
的面积就变为原来图像面积的四分之一。这被称为 Octave。连续进行这样
的操作我们就会得到一个分辨率不断下降的图像金字塔。我们可以使用函数
cv2.pyrDown() 和 cv2.pyrUp() 构建图像金字塔。

pyrUp(src, dst=None, dstsize=None, borderType=None)
功能：图像金字塔向上采样，图像尺寸加倍,分辨率不会增加（向上是针对尺寸而言的）。
参数：
    src：输入图像。
    dst：输出图像。
    dstsize：输出图像大小
    borderType：边界填充类型
    
pyrDown(src, dst=None, dstsize=None, borderType=None)
功能：图像金字塔向下采样，图像尺寸减半,分辨率降低（向下是针对尺寸而言的）。
参数：
    src：输入图像。
    dst：输出图像。
    dstsize：输出图像大小
    borderType：边界填充类型
    
    
拉普拉斯金字塔可以有高斯金字塔计算得来，公式如下：
Li = Gi - PyrUp(Gi+1)
拉普拉金字塔的图像看起来就像边界图，其中很多像素都是 0。他们经常
被用在图像压缩中。
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../images/meixi.jpg')

# 向下金字塔
DstpyrDown = cv.pyrDown(img)
# 向上金字塔
DstpyrUp = cv.pyrUp(DstpyrDown)

# 显示
cv.imshow("src img", img)
cv.imshow("pyrDown", DstpyrDown)
cv.imshow("DstpyrUp", DstpyrUp)
cv.waitKey(0)
cv.destroyAllWindows()
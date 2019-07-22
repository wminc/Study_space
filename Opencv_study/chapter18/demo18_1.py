# -*- coding:utf8 -*-
"""
Created on 2019/7/22 17:27

@author: WMaker
"""

'''
18.1 Sobel 算子和 Scharr 算子
Sobel 算子是高斯平滑与微分操作的结合体，所以它的抗噪声能力很好。
你可以设定求导的方向（xorder 或 yorder）。还可以设定使用的卷积核的大
小（ksize）。如果 ksize=-1，会使用 3x3 的 Scharr 滤波器，它的的效果要
比 3x3 的 Sobel 滤波器好（而且速度相同，所以在使用 3x3 滤波器时应该尽
量使用 Scharr 滤波器）。3x3 的 Scharr 滤波器卷积核如下：
         -3  0  3
x方向    -10  0 10
         -3  0  3 

        -3 -10 -3
y 方向  0 0 0 
        3 10 3

'''
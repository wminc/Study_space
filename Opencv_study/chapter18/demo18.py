# -*- coding:utf8 -*-
"""
Created on 2019/7/22 17:24

@author: WMaker
"""

'''
图像梯度
目标
• 图像梯度，图像边界等
• 使用到的函数有：cv2.Sobel()，cv2.Schar()，cv2.Laplacian() 等

原理
梯度简单来说就是求导。

OpenCV 提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr 和 Laplacian。
我们会意义介绍他们。
Sobel，Scharr 其实就是求一阶或二阶导数。
Scharr 是对 Sobel（使用小的卷积核求解求解梯度角度时）的优化。
Laplacian 是求二阶导数
'''



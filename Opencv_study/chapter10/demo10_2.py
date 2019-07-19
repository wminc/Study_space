# -*- coding:utf8 -*-
# author = 'WMaker'

'''
图像混合
这其实也是加法，但是不同的是两幅图像的权重不同，这就会给人一种混
合或者透明的感觉。图像混合的计算公式如下：
g(x) = (1-α)f0(x) + αf1(x)
通过修改 α 的值（0 → 1），可以实现非常酷的混合
'''

#现在我们把两幅图混合在一起。第一幅图的权重是 0.7，第二幅图的权重是 0.3。
# 函数 cv2.addWeighted() 可以按下面的公式对图片进行混合操作。
# dst = α · img1 + β · img2 + γ  这里 γ 的取值为 0。

import cv2
import numpy as np
img1=cv2.imread('../images/meixi.jpg')
img2=cv2.imread('../images/opencv.jpg')
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
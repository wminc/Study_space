# -*- coding:utf8 -*-
# @author = WMaker


import numpy as np

'''
Microsoft Windows [版本 10.0.10240]
(c) 2015 Microsoft Corporation. All rights reserved.

D:\ImageHandle\Opencv_space>ipython
Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.0.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: x = 5

In [2]: %timeit y=x**2
303 ns ± 0.418 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [3]: %timeit y=x*x
47.1 ns ± 0.0283 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [4]: import numpy as np


In [5]: z = np.uint8([5])

In [6]: %timeit y=z*z
473 ns ± 4.77 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [7]: %timeit y=np.square(z)
461 ns ± 4.65 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

'''
#注意：Python 的标量计算比 Nump 的标量计算要快。对于仅包含一两个元素的操作 Python 标量比 Numpy 的数组要快。
# 但是当数组稍微大一点时Numpy 就会胜出了。



'''
In [12]: import cv2

In [13]: img = cv2.imread('/images/meixi.jpg')

In [14]: %timeit z = cv2.countNonZero(img)
382 ns ± 1.16 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [15]: %timeit z = np.count_nonzero(img)
767 ns ± 0.774 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
'''
#注意：一般情况下 OpenCV 的函数要比 Numpy 函数快。所以对于相同的操作最好使用 OpenCV 的函数。
# 当然也有例外，尤其是当使用 Numpy 对视图（而非复制）进行操作时。
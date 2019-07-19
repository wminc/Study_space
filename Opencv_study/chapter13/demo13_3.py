# -*- coding:utf8 -*-
"""
Created on 2019/7/10 11:29

@author = WMaker
"""

'''
怎样找到要跟踪对象的 HSV 值？
这是我在stackoverflow.com上遇到的最普遍的问题。其实这真的很简单，
函数 cv2.cvtColor() 也可以用到这里。但是现在你要传入的参数是（你想要
的）BGR 值而不是一副图。例如，我们要找到绿色的 HSV 值，我们只需在终
端输入以下命令：
'''

import cv2
import numpy as np

# 以下二者一样
#green = np.array([0,255,0],dtype=np.uint8)
green=np.uint8([0,255,0])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

# green=np.uint8([[[0,255,0]]])
# hsv_green1 = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print(hsv_green1)
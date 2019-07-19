# -*- coding:utf8 -*-
# @author = WMaker

'''
13.2物体跟踪
现在我们知道怎样将一幅图像从 BGR 转换到 HSV 了，我们可以利用这
一点来提取带有某个特定颜色的物体。在 HSV 颜色空间中要比在 BGR 空间
中更容易表示一个特定颜色。在我们的程序中，我们要提取的是一个蓝色的物
体。下面就是就是我们要做的几步：
• 从视频中获取每一帧图像
• 将图像转换到 HSV 空间
• 设置 HSV 阈值到蓝色范围。
• 获取蓝色物体，当然我们还可以做其他任何我们想做的事，比如：在蓝色
物体周围画一个圈。


利用cv2.inRange函数设阈值，去除背景部分
  mask = cv2.inRange(hsv, lower, upper #lower20===>0,upper200==>0,
函数很简单，参数有三个
第一个参数：hsv指的是原图

第二个参数：lower指的是图像中低于这个lower的值，图像值变为0

第三个参数：upper指的是图像中高于这个upper的值，图像值变为0

而在lower～upper之间的值变成255

'''


import cv2
import numpy as np
cap=cv2.VideoCapture('../images/jiesen.mp4')
while(1):
    # 获取每一帧
    ret,frame=cap.read()
    # 转换到 HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # 设定紫色的阈值
    # 可以把图片转换为HSV图之后，获取该指定像素点的bgr值,再转成数组
    # 相当于对转成HSV之后的图构建掩模
    lower=np.array([60,60,150])
    upper=np.array([170,170,240])
    # 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower,upper)

    # 对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
    # 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    #k=cv2.waitKey(5)&0xFF
    k=cv2.waitKey(10)&0xFF
    print(k)
    if k==27:
        break

# 关闭窗口
cv2.destroyAllWindows()


#----------------------------------------------
image = cv2.imread('../images/jiesen.jpg')
# 转换到 HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 设定紫色的阈值
# 可以把图片转换为HSV图之后，获取该指定像素点的bgr值,再转成数组
# 相当于对转成HSV之后的图构建掩模
lower = np.array([110, 100, 200])
upper = np.array([170, 170, 240])
# 根据阈值构建掩模
mask = cv2.inRange(hsv, lower, upper)

# 对原图像和掩模进行位运算
res = cv2.bitwise_and(image, image, mask=mask)
# 显示图像
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()

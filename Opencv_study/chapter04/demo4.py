# coding:utf8

import cv2
import numpy as np

# 创建3X3的黑色方块
# 创建3X3的数组
# img = np.zeros((3,3),dtype=np.uint8)
# print(img)
# # 写入文件
# cv2.imwrite('../images/cv2_img1.jpg', img)
#
# print(img.shape)
# 返回行列
# # (3, 3)
# print(img.size)
# # 9

# # 利用cv2.cvtColor剪图像转成BRG格式
# img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# print(img)
# cv2.imwrite('../images/cv2_img2.jpg', img)
print('-----------------')
'''
imread(filename, flags=None)
filename:读取的文件名
flags:指定图像的读取方式
    cv2.IMREAD_COLOR : 默认使用该种标识。加载一张彩色图片，忽视它的透明度。
    cv2.IMREAD_GRAYSCALE : 加载一张灰度图。
    cv2.IMREAD_UNCHANGED : 加载图像，包括它的Alpha通道

'''

# img = cv2.imread('../images/cv2_img2.jpg',cv2.IMREAD_GRAYSCALE)
# print(img.shape)
# print(img.size)

'''
cv2.imShow():
    函数可以在窗口中显示图像。该窗口和图像的原始大小自适应
cv2.waitKey():
    cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫秒级。
    函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果
    按下任意键，这个函数会返回按键的 ASCII 码值，程序将会继续运行。如果没
    有键盘输入，返回值为 -1，如果我们设置这个函数的参数为 0，那它将会无限
    期的等待键盘输入。我们也可以将其设置为一个特定的键。
cv2.destroyALLWindows():
    销毁我们创建的所有窗口。
    如果要销毁任何特定窗口，请使用函数cv2.destroyWindow()，其中传递确切的窗口名称作为参数。
    (应该是使用创建窗口时所使用的窗口名称，字符串类型。)
注：
我们还可以使用另一种方法来加载图片：先创建一个窗口，之后在需要的时候将图像加载到该窗口。
说明：在这种情况下，用cv2.namedWindow()函数可以指定窗口是否可以调整大小。
在默认情况下，标志为cv2.WINDOW_AUTOSIZE。但是，如果指定标志为cv2.WINDOW_Normal，
则可以调整窗口的大小。当图像尺寸太大，并在窗口中添加跟踪条时，
这些操作可以让我们的工作更方便一点。
cv2.imshow()函数的第一个参数应和窗口的名称保持一致，这样才能将图片加载到窗口中去

'''
# cv2.imshow('imshow',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# #cv2.namedWindow('image', 0) #CV_WINDOW_NORMAL就是0
# # 设置窗口大小
# cv2.resizeWindow('image', 640, 480)
# # 改变窗口位置：left top
# cv2.moveWindow('image',1000,100)
#
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print('-----------------')
# bgrImg = cv2.imread('../images/cv2_img2.jpg')
# bgrByte = bytearray(bgrImg)
# bgrImageArray = np.array(bgrByte).reshape(3,3,3)
# print('读取bgr图的数组')
# print(bgrImageArray)
#
# grayImg = cv2.imread('../images/cv2_img2.jpg',cv2.IMREAD_GRAYSCALE)
# grayByte = bytearray(grayImg)
# grayImageArray = np.array(grayByte).reshape(3,3)
# print('读取灰度图的数组')
# print(grayImageArray)

print('-----------------')
image = cv2.imread('../images/cv2_img2.jpg')
image[0,1,1]=255
print(image)

# my_roi = image[0:3,0:3]

print('-----------------')
'''
shape:
    返回包含高度，宽度，通道的数组，
    如果图像为单色或者灰度图，将不包含通道值
size:
    指图像像素的大小
dtype:
    该属性会得到图像的数据类型（通常为无符号的整数类型和该类型占用的位数，如unit8）
'''
print(image.shape)

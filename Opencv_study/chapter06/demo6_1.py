# coding:utf8

import cv2
import numpy as np

'''
创建图形以及写入文本
'''

# 创建一个512X512的黑色的brg图
img = np.zeros((512, 512, 3), np.uint8)

#print(img)
#print('-------------------------------')
'''
绘制线

line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
img：要画的图形所在的矩形或图像
pt1: 起点
pt2: 终点
color：颜色，如 (0, 0, 255) 红色，BGR
thickness：如果给一个闭合图形设置为 -1，那么这个图形就会被填充,正值表示边框宽度
lineType：线型
shift：小数点位数
'''
# 画一条宽度为1 的从（0,0）到（511,511）蓝色的线
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), thickness=1)
# cv2.imshow('123', img)
# cv2.waitKey(0)


'''
绘制矩形

rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
img：要画的图形所在的矩形或图像
pt1: 起点（左上角点坐标）
pt2: 终点（右下角点坐标）
color：圆边框颜色，如 (0, 0, 255) 红色，BGR
thickness：如果给一个闭合图形设置为 -1，那么这个图形就会被填充,正值表示边框宽度
lineType：线型
shift：小数点位数
'''
# 画一条宽度为3 的从（384,0）到（510,128）绿色矩形
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3,0)


'''
绘制圆

circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
img：要画的图形所在的矩形或图像
center：圆心坐标，如 (100, 100)
radius：半径，如 10
color：圆边框颜色，如 (0, 0, 255) 红色，BGR
thickness：如果给一个闭合图形设置为 -1，那么这个图形就会被填充,正值表示圆边框宽度. 负值表示画一个填充圆形
lineType：圆边框线型
shift：圆心坐标和半径的小数点位数
'''
# 画一条宽度为-1 的圆心(447,63)红色圆
cv2.circle(img,(447,63), 63, (0,0,255), 1,8)


'''
绘制椭圆

ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
img：要画的图形所在的矩形或图像
center：椭圆中心坐标，如 (100, 100)
axes: 轴长(长轴长、短轴长)
angle: 角度是椭圆逆时针方向旋转的角度
startAngle,endAngle:从长轴顺时针方向测量的椭圆弧的开始和结束。即给出0和360表示整个椭圆
color：颜色，如 (0, 0, 255) 红色，BGR
thickness：如果给一个闭合图形设置为 -1，那么这个图形就会被填充,正值表示边框宽度
lineType：线型
shift：小数点位数
'''
# 绘制中心(256,256)长轴100，短轴50，无旋转角度，完整的填充黄色椭圆
cv2.ellipse(img,(256,256),(100,50),10,0,360,(0,255,255),-1)


'''
绘制多边形

polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None):
img：要画的图形所在的矩形或图像
pts：多边形的点集合
isClosed: 是否闭合
color：颜色，如 (0, 0, 255) 红色，BGR
thickness：如果给一个闭合图形设置为 -1，那么这个图形就会被填充,正值表示边框宽度
lineType：线型
shift：小数点位数

提示：
1. 如果第三个参数是false，那么将得到一个折线连接所有的点，而不是一个封闭的图形。
2. cv2.polyline()可用于绘制多条线。只需创建要绘制的所有线条的列表，并将其传递给函数。
   所有的线都将单独划出。与为每一行调用cv2.line()相比，绘制一组直线的方法更好、更快

'''
#数组的数据类型必须为 int32
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print(pts)
pts = pts.reshape((-1,1,2))
print(pts)
cv2.polylines(img,[pts],True,(0,255,255))

'''
为图片添加文本信息

putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

img：要写入文本所在的矩形或图像
text：要写入的文本数据
org: 要放置它的位置坐标(即数据开始的左下角)
fontFace: 字体类型
fontScale: 字体大小
color：颜色
thickness：不能为负数
lineType：线型，可为
bottomLeftOrigin:
'''

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),10,4)

# 可以一块显示
cv2.imshow('123', img)
cv2.waitKey(0)

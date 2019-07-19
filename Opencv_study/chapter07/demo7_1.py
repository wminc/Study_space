# coding:utf8

import cv2
import numpy as np

'''
控制鼠标动作

首先，需要创建一个鼠标回调函数，在发生鼠标相关事件时执行该函数。
鼠标事件可以是任何与鼠标相关的东西，如鼠标左键按下，鼠标左键弹起，左键双击等等.
它给出了每个鼠标事件的坐标(x，y)。有了这个事件和坐标定位，我们可以做任何我们想做的事。
有关鼠标的所有相关回调函数有：
'EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP'

创建鼠标回调函数有一个特定的格式，它的调用形式基本都是相同的。
只不过在函数的功能上有所不同。

'''


# 鼠标回调函数做了一件动作（双击鼠标左键），它画了一个圆圈。
def draw_circle1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

# Create a black image, a window and bind the function to window
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle1)
#
# while (1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()




drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1

# mouse callback function
def draw_circle2(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # 按下鼠标左键获取起点位置
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y


    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # 移动，mode==true画矩形否则画圆形
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    # 松了鼠标左键，mode==true画矩形否则画圆形
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)



img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle2)
# 在主循环中，我们应该为键“m”设置一个键盘绑定，以在矩形和圆形之间切换
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        #按下ESC退出
        break
cv2.destroyAllWindows()

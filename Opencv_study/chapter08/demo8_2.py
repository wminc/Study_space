# -*- coding: utf-8 -*-

import cv2
import numpy as np


def nothing(x):
    pass


# 拓展，选择颜色，并用该颜色在画布上画圆或矩形

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
def draw_circle2(event, x, y,flags, param):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    bgr = (b, g, r)

    global ix, iy, drawing, mode

    # 按下鼠标左键获取起点位置
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # 移动，mode==true画矩形否则画圆形
            if mode == True:
                cv2.rectangle(draw_board, (ix, iy), (x, y), bgr, -1)
            else:
                cv2.circle(draw_board, (x, y), 5, bgr, -1)
    # 松了鼠标左键，mode==true画矩形否则画圆形
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(draw_board, (ix, iy), (x, y), bgr, -1)
        else:
            cv2.circle(draw_board, (x, y), 5, bgr, -1)


draw_board=np.zeros((300,512,3),np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

cv2.setMouseCallback('image', draw_circle2)

while(1):
    cv2.imshow('image', draw_board)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        #按下ESC退出
        break

cv2.destroyAllWindows()

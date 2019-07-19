# -*- coding:utf8 -*-
"""
Created on 2019/7/10 14:20

@author: WMaker
"""


'''
从文件中播放视频
与从摄像头中捕获一样，你只需要把设备索引号改成视频文件的名字。在
播放每一帧时，使用 cv2.waiKey() 设置适当的持续时间。如果设置的太低视
频就会播放的非常快，如果设置的太高就会播放的很慢（你可以使用这种方法
控制视频的播放速度）。通常情况下 25 毫秒就可以了。
'''

import cv2

# 打开视频文件,视频文件总会结束，需要判断是否结尾
cap = cv2.VideoCapture('../images/jiesen.mp4')
frame_num = cap.get(7)
print(frame_num)
while(1):
    ret,frame = cap.read()
    if ret==True:
        cv2_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('GRAY_Mp4',frame)

        if cv2.waitKey(1)&0xFF==ord('q'):
            break

        # next_frame_index = cap.get(1)
        # print(next_frame_index)

    else:
        break

cap.release()
cv2.destroyAllWindows()
# -*- coding:utf8 -*-
"""
Created on 2019/7/10 14:06

@author = WMaker
"""

'''
视频
目标
• 学会读取视频文件，显示视频，保存视频文件
• 学会从摄像头获取并显示视频
• 你将会学习到这些函数：cv2.VideoCapture()，cv2.VideoWrite()

5.1 用摄像头捕获视频
我们经常需要使用摄像头捕获实时图像。OpenCV 为这中应用提供了一个
非常简单的接口。让我们使用摄像头来捕获一段视频，并把它转换成灰度视频
显示出来。从这个简单的任务开始吧。
为了获取视频，你应该创建一个 VideoCapture 对象。他的参数可以是
设备的索引号，或者是一个视频文件。设备索引号就是在指定要使用的摄像头。
一般的笔记本电脑都有内置摄像头。所以参数就是 0。你可以通过设置成 1 或
者其他的来选择别的摄像头。之后，你就可以一帧一帧的捕获视频了。但是最
后，别忘了停止捕获视频。
'''

import cv2

# 打开摄像机
#cap = cv2.VideoCapture(0)

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


'''
cap.read() 返回一个布尔值（True/False）。
如果帧读取的是正确的，就是 True。所以最后你可以通过检查他的返回值来查看视频文件是否已经到了结尾。
有时 cap 可能不能成功的初始化摄像头设备。这种情况下上面的代码会报错。
你可以使用 cap.isOpened()，来检查是否成功初始化了。如果返回值是True，那就没有问题。
否则就要使用函数 cap.open()。
你可以使用函数 cap.get(propId) 来获得视频的一些参数信息。
这里propId 可以是 0 到 18 之间的任何整数。每一个数代表视频的一个属性，见
下表

其中的一些值可以使用 cap.set(propId,value) 来修改，value 就是你想要设置成的新值。
例如，我可以使用 cap.get(3) 和 cap.get(4) 来查看每一帧的宽和高。
默认情况下得到的值是 640X480。但是我可以使用 ret=cap.set(3,320)
和 ret=cap.set(4,240) 来把宽和高改成 320X240。

• CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
• CAP_PROP_POS_FRAMES 下一帧的索引
• CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
• CAP_PROP_FRAME_WIDTH 某一帧的宽度
• CAP_PROP_FRAME_HEIGHT 某一帧的高度
• CAP_PROP_FPS Frame rate.
• CAP_PROP_FOURCC 4-character code of codec.
• CAP_PROP_FRAME_COUNT 统计视频帧数
• CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
• CAP_PROP_MODE Backend-specific value indicating the current capture mode.
• CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
• CAP_PROP_CONTRAST Contrast of the image (only for cameras).
• CAP_PROP_SATURATION Saturation of the image (only for cameras).
• CAP_PROP_HUE Hue of the image (only for cameras).
• CAP_PROP_GAIN Gain of the image (only for cameras).
• CAP_PROP_EXPOSURE Exposure (only for cameras).
• CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
• CAP_PROP_WHITE_BALANCE Currently unsupported
• CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
'''

# -*- coding:utf8 -*-
"""
Created on 2019/7/10 14:47

@author: WMaker
"""

'''
保存视频
在我们捕获视频，并对每一帧都进行加工之后我们想要保存这个视频。对
于图片来说很简单只需要使用 cv2.imwrite()。但对于视频来说就要多做点工作。
这次我们要创建一个 VideoWriter 的对象。我们应该确定一个输出文件的名字。
接下来指定 FourCC 编码（下面会介绍）。播放频率和帧的大小也都需要确定。
最后一个是 isColor 标签。如果是 True，每一帧就是彩色图，否则就是灰度图。
FourCC 就是一个 4 字节码，用来确定视频的编码格式。
可用的编码列表可以从fourcc.org查到。这是平台依赖的。
下面这些编码器对我来说是有用个。
• In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is
more preferable. MJPG results in high size video. X264 gives
very small size video)
• In Windows: DIVX (More to be tested and added)
• In OSX : (I don’t have access to OSX. Can some one fill this?)
FourCC 码以下面的格式传给程序，以 MJPG 为例：
cv2.VideoWriter_fourcc('M','J','P','G') 或者 cv2.cv.FOURCC(*'MJPG')。
下面的代码是从摄像头中捕获视频，沿水平方向旋转每一帧并保存它。



cv2.flip() 图像翻转
flipCode	    Anno
   1	      水平翻转
   0	      垂直翻转
  -1	    水平垂直翻转
'''

import cv2

# 打开视频文件,视频文件总会结束，需要判断是否结尾
cap = cv2.VideoCapture('../images/jiesen.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 获取窗口大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

# 设置帧率
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)


out = cv2.VideoWriter('../images/output.avi',fourcc, fps, size)

while(1):
    ret,frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
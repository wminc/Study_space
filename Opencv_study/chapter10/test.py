# -*- coding:utf8 -*-
# author = 'WMaker'

from PIL import Image
import cv2

# 加载图像

# PIL图像合并
show_image = Image.open('../images/meixi.jpg')
tree_Image = Image.open('../images/Ball.png')
tree_Image = tree_Image.convert('RGBA')
# tree_Image=tree_Image.resize((200,200),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
show_image.paste(tree_Image,(0,0),tree_Image)
show_image.show()

# opencv图像合并add()
img1 = cv2.imread('../images/meixi.jpg')
img2 = cv2.imread('../images/Ball.png')
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

dst = cv2.add(roi,img2)
cv2.imshow('dst',dst)
cv2.waitKey(0)

img1[0:rows, 0:cols ] = dst
cv2.imshow('img1',img1)
cv2.waitKey(0)
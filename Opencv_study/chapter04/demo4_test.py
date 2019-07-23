# -*- coding:utf8 -*-
"""
Created on 2019/7/23 13:36

@author: WMaker
"""
'''
cv2和plt
'''
import cv2
from matplotlib import pyplot as plt

img_cv2 = cv2.imread('../images/bankcard.jpg')

cv2.imshow('img',img_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 转成rgb
# img_rgb = img_cv2[:,:,[2,1,0]]
img_rgb = cv2.cvtColor(img_cv2,cv2.COLOR_BGR2RGB)


plt.subplot(1, 1, 1), plt.imshow(img_rgb), plt.title('Img')
plt.xticks([]), plt.yticks([])
plt.show()

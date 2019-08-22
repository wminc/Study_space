# -*- coding:utf8 -*-
# Author = 'WMaker'
# Create Time：

'''
Introduction：
'''

import numpy as np


arr = np.array([[1,2,3],[4,5,6]])

print(arr)
print('\n')

# 加法运算
data_arr = arr + arr
print(data_arr)
print('\n')

# 减法运算
d_arr = arr - arr
print(d_arr)
print('\n')

# 乘法运算
arr_10 = arr*10
print(arr_10)

print('\n')
arr_arr = arr*arr
print(arr_arr)
print('\n')

# 除法运算
arr_divide = 1 / arr
print(arr_divide)
print('\n')

# 平方根运算
arr_square_root = arr ** 0.5
print(arr_square_root)

# 比较运算
arr2 = np.array([[0,4,1],[7,6,12]])
print(arr2)
arr_compare = arr2 > arr
print(arr_compare)
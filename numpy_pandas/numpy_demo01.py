# -*- coding:utf8 -*-
# Author = 'WMaker'
# Create Time：2019/08/13

'''
Introduction：
'''

import numpy as np

# 生成随机数组
data_arr = np.random.randn(2,3)
print(data_arr)

# shape表示该数组大小形状(row,col)
data_arr_shape = data_arr.shape
print(data_arr_shape)

# dtype表示data type
# 除非主动声明，否则np.array会自动给data搭配适合的类型，并保存在dtype里
data_arr_dtype = data_arr.dtype
print(data_arr_dtype)



print('-'*50)
# 创建n维数组
# 列表转数组
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print(arr1.shape)
# 数组的维度
print(arr1.ndim)
print(arr1.dtype)

print('-'*20)

# 多维列表转数组
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.shape)
# 数组的维度
print(arr2.ndim)
print(arr2.dtype)

print('-'*20)

data3 = [[[1,1,1],[2,2,2],[3,3,3]],[[3,3,3],[4,4,4],[5,5,5]]]
arr3 = np.array(data3)
print(arr3)
print(arr3.shape)
print(arr3.ndim)
print(arr3.dtype)

print('-'*20)

# np.zeros()
arr_zero1 = np.zeros(10)
print(arr_zero1)

arr_zero2 = np.zeros((3,6))
print(arr_zero2)

arr_zero3 = np.zeros((3,1,2))
print(arr_zero3)

print('-'*20)

# np.ones()
arr_one1 = np.ones(10)
print(arr_zero1)

arr_one2 = np.ones((3,6))
print(arr_one2)

arr_one3 = np.ones((3,1,2))
print(arr_one3)

print('-'*20)

# np.empty()
arr_empty1 = np.empty((2,3,2))
print(arr_empty1)

print('-'*20)

# np.arange()
arr_arange = np.arange(10)
print(arr_arange)

print('-'*50)
# dtype

arr_dtype1 = np.array([1,2,3],dtype=np.float64)
print(arr_dtype1.dtype)

print('-'*20)

arr_dtype2 = np.array([1,2,3], dtype=np.int32)
print(arr_dtype2.dtype)

print('-'*20)

# astype()
arr_int32 = np.array([1,2,3,4,5])
float_arr = arr_int32.astype(np.float64)
print(float_arr)
print(float_arr.dtype)

print('-'*20)

arr_float64 = np.array([3.7,1.2,-2.6,-0.5])
int_arr = arr_float64.astype(np.int32)
print(int_arr)
print(int_arr.dtype)

print('-'*20)

arr_string = np.array(['1.25','-9.6','13'],dtype=np.string_)
print(arr_string)
float_arr = arr_string.astype(float)
print(float_arr)
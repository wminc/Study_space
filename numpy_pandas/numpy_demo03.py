# -*- coding:utf8 -*-
# Author = 'WMaker'
# Create Time：

'''
Introduction：
'''

import numpy as np

arr = np.arange(10)
print(arr)

print(arr[5])

print(arr[5:8])

arr[2:5] = 77

print(arr)

# python内建的list与numpy的array有个明显的区别，
# 这里array的切片后的结果只是一个views(视图)，用来代表原有array对应的元素，而不是创建了一个新的array。
# python中切片之后相当于创建了新的list

arr_slice = arr[5:8]

print('arr_slice',arr_slice)

# 如果我们改变arr_slice的值，会反映在原始的数组arr
arr_slice[1] = 1997
print('arr_slice',arr_slice)
print('arr',arr)

# 当然如果想要复制,可以使用copy()方法
arr_copy = arr.copy()
arr_copy[1] = 1997
print(arr_copy)
print(arr)

print('-'*50)
# 二维数组的索引

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[2])
print()
print(arr2d[2][1])
print()
# 另一种访问方式
print(arr2d[2,1])
print()

print('-'*50)
# 三维数组的索引
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print('\n')
# 三维数组的单索引是二维数组
print(arr3d[0])
print('\n')
# 三维数组的双索引是一维数组
print(arr3d[0][1])

print('-'*50)
# 二维数组切片

# 选中arr2d的前两行
arr2d_slice = arr2d[:2]
print(arr2d_slice)
print()
# 前两行，第二列之后
arr2d_slice2 = arr2d[:2, 1:]
print(arr2d_slice2)
print()
# 第二行的前两列
print(arr2d[1, :2])
print()

# 前两行第三列
print(arr2d[:2, 2])
print()

# 全部行的第三列
print(arr2d[:, 2])
print()

print('-'*50)
# 布尔索引

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names)

arr_data = np.random.randn(7, 4)
print(arr_data)
print()
# 每一个name对应data数组中的一行，我们想要选中name为'Bob'的所有行。
# 就像四则运算，用比较运算符（==）：
names == 'Bob'
# 输出boolean值的列表
print(names == 'Bob')
print()
# 用这个布尔数组当做索引
# 输出arr_data中对应为true的行
print(arr_data[names == 'Bob'])
print()

print(arr_data[names == 'Bob', 2:])
print()

#选中除了'Bob'外的所有行
print(arr_data[names != 'Bob'])
print()

cond = names=='Bob'
print(arr_data[~cond])
print()

mask = (names == 'Bob') | (names == 'Will')
print(mask)
print()

print(arr_data[mask])
print()

# 让所有负数变为0
arr_data[arr_data < 0] = 0
print(arr_data)

print('-'*50)

# 花式索引fancy indexing
# 和切片不同，得到的是一个新的array
arr_empty = np.empty((8,4))
print(arr_empty)
print()

for i in range(8):
    arr_empty[i] = i

print(arr_empty)
print()

arr_new = arr_empty[[4,3,0,5]]
print(arr_new)

arr_new2 = arr_empty[[-3, -5, -7]]
print(arr_new2)

arr = np.arange(32).reshape((8, 4))
print(arr)
print()
# [ 4, 23, 29, 10]分别对应(1, 0), (5, 3), (7, 1), (2, 2)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print()

# 先从arr中选出[1, 5, 7, 2]这四行,
# 然后[:, [0, 3, 1, 2]]表示选中所有行，但是列的顺序要按0,3,1,2来排
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

print('-'*50)

# 转置
arr = np.arange(8).reshape((4, 2))
print(arr)
print()
print(arr.T)
print()

# 计算矩阵乘法的时候，用np.dot
# 矩阵相乘只有在第一个矩阵的列数和第二个矩阵的行数相同时才有意义 
print(np.dot(arr.T, arr))
print()

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print()

print('-'*50)

# transpose()
# 二维数组中transpose（X，Y）函数和矩阵的转置是一个意思，行为X轴，列为Y轴
# X轴用0表示，Y轴用1表示；
# 例如：如果transport（1，0）表示行与列调换了位置
arr = np.arange(15).reshape((3, 5))   
print(arr)
print()
print(arr.T)
print()
print(arr.transpose(1, 0))
print()
print('-'*20)
# 三维数组中transpose()它有三个维度；相当于有X轴，Y轴，Z轴；三个轴之间的相互转换；
# 同样，X轴用0表示，Y轴用1表示；Z轴用2来表示；如图 ./三维数组.png
arr = np.arange(24).reshape((2, 3, 4))
print(arr)
print()
# transport（0，2，1）：表示Y轴与Z轴发生轴变换
vc1 = arr.transpose(0,2,1)
print(vc1)
print()
# transport（2，1，0）：表示X轴与Z轴发生轴变换
vc2 = arr.transpose(2,1,0)
print(vc2)
print()
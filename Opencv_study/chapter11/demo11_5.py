# -*- coding:utf8 -*-
# @author = WMaker

'''
效率优化技术
有些技术和编程方法可以让我们最大的发挥 Python 和 Numpy 的威力。
我们这里仅仅提一下相关的，你可以通过超链接查找更多详细信息。我们要说
的最重要的一点是：首先用简单的方式实现你的算法（结果正确最重要），当结
果正确后，再使用上面的提到的方法找到程序的瓶颈来优化它。
1. 尽量避免使用循环，尤其双层三层循环，它们天生就是非常慢的。
2. 算法中尽量使用向量操作，因为 Numpy 和 OpenCV 都对向量操作进行
了优化。
3. 利用高速缓存一致性。
4. 没有必要的话就不要复制数组。使用视图来代替复制。数组复制是非常浪
费资源的。
就算进行了上述优化，如果你的程序还是很慢，或者说大的训话不可避免的话，
你你应该尝试使用其他的包，比如说 Cython，来加速你的程序。
'''
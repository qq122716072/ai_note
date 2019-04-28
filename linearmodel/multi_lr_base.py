import numpy as np

#随机生成3*2的矩阵
print(np.random.rand(3,2))
#生成值均为1 的10*1的矩阵
print(np.ones((10,1)))
#两个矩阵相乘
a = np.array([1,2,3,4,5,6]).reshape(3,2)
b = np.array([1,2]).reshape(2,1)
print(a.dot(b))
#矩阵转置
print(a)
print(a.T)

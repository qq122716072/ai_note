import numpy as np

a = np.array([1,2,3,4,5,6])
#变矩阵
b = a.reshape(3,2)
print(b)
print(np.sum(b, axis=1))

p = np.array([2,2])
print(p-b)

#距离计算 欧氏距离

print(np.sum((p-b)**2, axis=1)**0.5)
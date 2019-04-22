import numpy as np

a = np.array([1,2,3,4,5])
print(type(a))

#均值
print(a.mean())
print(np.mean(a))

#排序
print(a.argsort())
print(np.argsort(a))

print(a*2)
print([1,2,3,4,5]*2)
print(a**2)
b = np.array([9,8,7,6,5])
print(b-a)
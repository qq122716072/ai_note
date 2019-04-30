import numpy as np
import matplotlib.pyplot as plt

'''
多元线性回归
'''

#随机生成100*1的矩阵 随机数为0到2之间的数
X_a = 2 * np.random.rand(100, 1)
#生成100*1的每个值都为1的矩阵
X_b = np.ones((100,1))
#合并两个矩阵
X = np.c_[np.ones((100, 1)), X_a]
#生成x所对应的y  np.random.randn(100, 1)生成100*1的随机数 服从正太分布
y = 5 + 4 * X_a + np.random.randn(100,1)
#根据解析解 求出theta的值  np.linalg.inv求逆的方法
# theta_best = (X.T.dot(y)) / X.T.dot(X)
theta_best = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y))
print(theta_best)

X_new_a = np.array([[0], [2]])
X_new = np.c_[np.ones((2, 1)), X_new_a]
y_predict = X_new.dot(theta_best)

print(y_predict)

plt.plot(X_new_a, y_predict, 'r-')
plt.plot(X, y, 'b.')
plt.axis([0, 2, 0, 15])
plt.show()



import numpy as np

"""
自己实现sklearn中的现行回归模型
"""


X = [4,8,5,10,12]
y = [20,50,30,70,60]

class LinearRegression(object):
    def __init__(self):
        self.w = 0
        self.b = 0

    """
    训练
    """
    def fit(self,X,y):
        x_mean = np.mean(X)
        y_mean = np.mean(y)
        # 分子,分母
        numbeartor, denominator = 0, 0
        for i in range(len(X)):
            # sklearn中用的这种方法
            numbeartor += X[i] * y[i] - y_mean * X[i]
            denominator += X[i] ** 2 - x_mean * X[i]
        self.w = numbeartor / denominator
        self.b = y_mean - self.w * x_mean

    """
    预测
    """
    def predict(self,test):
        return self.w * test + self.b


model = LinearRegression()
model.fit(X, y)
predict = model.predict(15)
print(predict)

import numpy as np

X = [4,8,5,10,12]
y = [20,50,30,70,60]

#训练
def linear_regresion(X,y):
    """
    简单线性回归模型
    :param X: 输入数据
    :param y: 输出数据
    :return: 返回简单线性回归的参数  w,b
    """
    x_mean = np.mean(X)
    y_mean = np.mean(y)
    #分子,分母
    numbeartor,denominator=0,0
    for i in range(len(X)):
        # numbeartor += (X[i]-x_mean)*(y[i]-y_mean)
        # denominator += (X[i]-x_mean)**2
        #sklearn中用的这种方法
        numbeartor += X[i]*y[i]-y_mean*X[i]
        denominator += X[i]**2-x_mean*X[i]
    w = numbeartor/denominator
    b = y_mean-w*x_mean
    return w,b

def predict(w,b,test):
    return w*test+b


#训练模型
w,b = linear_regresion(X,y)
print(w,b)
print(predict(w,b,15))
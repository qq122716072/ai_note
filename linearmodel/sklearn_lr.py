from sklearn.linear_model import LinearRegression

X = [[4],[8],[5],[10],[12]]
y = [20,50,30,70,60]

model = LinearRegression()
#训练模型
model.fit(X,y)
#预测
pred = model.predict([[15]])
print(pred)
# coef_参数 intercept_截距
print(model.coef_,model.intercept_)

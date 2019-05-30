import numpy as np
import pandas as pd

# a = np.array([1,2,3,4,5])
# print(a)
#
# data = pd.Series([1,3,5,7,9])
# print(data)
# print(data.values)
# print(data.index)
# print(data[0])
# print(data[0:3])

#指定index对象
data = pd.Series([1,3,5,7,9],index=['one', 'two', 'three', 'four', 'five'])
print(data)
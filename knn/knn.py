"""
knn
样本集
X = [[1,1],[1,1.5],[2,2],[4,3],[4,4]]
Y =['A','A','A','B','B']
测试样本:
t=[3,2] 属于哪个类型
设k=3

knn的实现：
   1.计算待分类样本和训练样本之间的距离
   2.对所有的距离进行排序
   3.取前k个最近的样本：计算每个类别的样本的个数

        1)根据排序的下标 取出原数据属于哪个类别
        2)将相同类别的元素个数加和--字典
   4.投票
"""

import numpy as np
import operator

def knn_classify(x,y,testdata,k):
    """
    knn分类器 通过欧氏距离来衡量距离远近
    :param x: 样本集的输入数据
    :param y: 样本集的输出数据
    :param testdate: 待分类数据
    :param k: 最近的几个点
    :return: 返回待分类数据的类别
    """
#     # 1.计算待分类样本和训练样本之间的距离
#     distance = np.sum((testdata - x) ** 2, axis=1) ** 0.5
#     # 2.对所有的距离进行排序
#     sortedIndex = np.argsort(distance)
#     # 3.取前k个最近的样本：计算每个类别的样本的个数
#         # 1)根据排序的下标取出原数据属于哪个类别
#         # 2)将相同类别的元素个数加和 - -字典
#     classLableCount = {}
#     for i in range(k):
#         lable = y[sortedIndex]
#         classLableCount[lable] = classLableCount.get(lable,0)+1
#     # 4.投票
#     return sorted(classLableCount.items(),key=operator.itemgetter(1),reverse=True)[0][0]
#
# if __name__=="__main__":
#     X = np.array([[1,1],[2.2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]])
#     y = ['A','A','A','B','B']
#     test = np.array([3,2])
#     pred = knn_classify(X,y,test,3)
#     print(pred)

    # 1.计算待分类样本和训练样本之间的距离
    distance = np.sum((testdata-x)**2,axis=1)**0.5
    print(distance)
    # 2.对所有的距离进行排序
    sortedIndex = np.argsort(distance)
    # 3.取前k个最近的样本：计算每个类别的样本的个数
    # 1)根据排序的下标取出原数据属于哪个类别
    # 2)将相同类别的元素个数加和 - -字典
    classLabelCount = {}
    for i in range(k):
        label = y[sortedIndex[i]]
        classLabelCount[label] = classLabelCount.get(label,0)+1
    # 4.投票
    return sorted(classLabelCount.items(),key=operator.itemgetter(1),reverse=True)[0][0]
if __name__=="__main__":
    X = np.array([[1,1],[1,1.5],[2,2],[4,3],[4,4]])
    y =['A','A','A','B','B']
    test = np.array([3,2] )
    pred = knn_classify(X,y,test,3)
    print(pred)


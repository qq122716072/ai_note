# print("hello,python")
#
# print("hello", "world", "python", sep="\t")
#
# print("-----end", end="\n")
#
# print(10/3)
#
# print(10//3)
#
# print(2*3)
# print(2**3)
#
# #三目运算符
# print(1 if 3>2 else 0)
#
# a=10
# b=100
# print(a,b)
# a, b = b, a
# print(a, b)
#
# if 3>2:
#     print("true")
# else:
#     print("false")
#
# for i in range(10):
#     print(i)
#
# d = {"a" : 10, "b" : 6, "c" : 4, "d" : 2}
# print(d.get("a"), "111")
# print(d["a"])
# print(d.get("e", "222"))
# for i in d.items():
#     print(i)
#
#
# #定义函数
# def show(name):
#     print(name)
#     return 1
#
# show("tom")
# print(show("jim"))

import python_basic.add as cadd
from python_basic.add import add

if __name__ == "__main__":
    print(cadd.add(3, 4))
    print(add(2, 4))
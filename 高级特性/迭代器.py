#可以直接作用于for循环的对象统称为可迭代对象：Iterable。
from collections.abc import Iterable
from collections.abc import Iterator

#isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(1,10)), Iterable))
print(isinstance(100, Iterable))
print("-------------------")
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance(100, Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((x for x in range(10)), Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#iter()函数可以把list dict str 等可迭代对象编程迭代器


str1 = "123.456"
print(str1.split(".",1))




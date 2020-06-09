#列表生成式即List Comprehensions 是python中内置的 用来创建list生成式
print(list(range(1,10)))


l1 = [x * x for x in range(1,10)]
print(l1)

#仅选出偶数的平方
l2 = [x * x for x in range(1,5) if x % 2 == 0]
print(l2)

#两层循环
l3 = [m + n for m in 'huang' for n in 'shang']
print(l3)

import os
#listdir 列出文件和目录
print([d for d in os.listdir('.')])

#同时迭代字典中的key和value
d = {
    'one' : '1',
    'two' : '2',
    'three' : '3'
    }
for k, v in d.items():
    print(f'{k} = {v}')

#使用两个变量生成list
print([k + '=' + v for k,v in d.items()])

#所有字符串变小写
L = ['HUANG','SHANG']
print([s.lower() for s in L])

#可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

#ex  修改列表生成式，通过添加if语句保证列表生成式正确执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L1)
print(L2)


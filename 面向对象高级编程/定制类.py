#__xxx__的变量和函数名都要注意，这些是有特殊用途的

#__str__
class Student():
    def __init__(self,name):
        self.name = name
    #定义__str__方法，返回一个好看的字符串,该方法在打印一个类的实例对象时，会被自动调用，并返回一个字符串。
    def __str__(self):
        return f'Student object name: {self.name}'
    __repr__ = __str__
'''
直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。通常__str__()和__repr__()代码都是一样的
'''
print(Student('hs'))

'''
__iter__
如果一个类想被用于for in 循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会
不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

'''
class Fib():
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器 a，b

    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

#Fib实例虽然能作用于for循环，但是无法像list一样使用，如实现不了取指定位元素，实现这个功能可以使用__getitem__()方法
class Fib1():
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a,b = b, a + b
        return a


f = Fib1()
print(f[0])
print(f[1])
print(f[2])

#list的切片操作对于Fib会报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
#故要做判断
class Fib2():
    def __getitem__(self, n):
        if isinstance(n, int): #此处n为索引
            a, b = 1, 1
            for x in range(n):
                a,b = b, a + b
            return a
        if isinstance(n,slice): #此处n为切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f2 = Fib2()
print(f2[0:5])
'''
如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
'''


#当调用不存在的方法或者属性时，就会报错。要避免这个错误，出了可以添加属性之外，还可以写一个__getatter__()方法，动态返回一个属性
#只有在没有找到属性的情况下才调用__getattr__,已有的属性，比如name，不会在__getattr__中查找
class Student1():
    def __init__(self):
        self.name = 'hs'

#当调用不存在的属性时，解释器会调用__getattr__(self,'score')来尝试获得属性，这样就回返回score的值
    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda : 21
        raise AttributeError('\'Student1\' object has no attribute \'%s\'' % item)

hs = Student1()
print(hs.name)
print(hs.score)
print(hs.age())#也可以返回一个函数，不过调用方式要改为hs.age()
# print(hs.abc)#当调用不存在的属性，且没有在__getattr__定义过默认返回None，可以对方法修改，抛出AttributeErrpr错误

#利用完全动态的__getattr__,我们可以写出一个链式调用：
class Chain():
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    __repr__ = __str__

print(Chain().users('hs').repos)
'''
第一步，初始化一个实例
urls = Chain() 

第二步，查找urls的属性users，没找到定义的属性便调用__getattr__方法，返回一个函数调调用
urls = urls.users
这一步调用了Chain()，并把users属性作为参数传递了进去，即Chain(users),最终返回/users

第三步
Urls = urls('hs')
对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

最后一步
urls = u.repos

'''

#任何类只需要定义一个__call__()方法，就可以对实例进行调用。
class Student3():
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print(f'My name is {self.name}')
zfy = Student3('zfy')
zfy()
print(callable(Student3))#判断是否为可调用对象




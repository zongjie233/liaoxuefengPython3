from 继承和多态 import *
#判断对象类型，使用type()函数
print(type(123))

#如果一个变量指向函数或者类，也可用type()判断
print(type(max))

#type返回值为type类
print(type(type(123)))

#判断一个对象是否为函数时，使用types模块中定义的常量
import types
def fn():
    pass


print(type(fn))
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x :x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print('------------------------')


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
a = Animal()
b = Dog()
c = Husky()
print(isinstance(a,Animal))
print(isinstance(b,Animal))
print(isinstance(c,Animal))
print('=*******=')
print(isinstance(b,Husky))
#也可用isinstance()实现type()的功能,总是优先使用isinstance()
print(isinstance('a',str))
print(isinstance(123,int))
print('-----------')

#也可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 4],(list, tuple)))
print(isinstance((1, 2, 4),(list, tuple)))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，返回一个包含字符串的list
print(dir('abc'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的
#下述两种方法实现同样的功能
print(len('abc'))
print('abc'.__len__())

#在自己编写类的时候，如果想用类似len(obj)的话，可以自己写一个__len__()方法
class MyDog():
    def __len__(self):
        return 20

dog = MyDog()
print(len(dog))

# 配合getattr()、setattr()以及hasattr()，直接操作一个对象的状态
class MyObject():
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj,'x')) #有属性'x'吗
print(obj.x)
print(hasattr(obj,'y')) #有属性'y'吗
setattr(obj,'y',20) #设置一个属性'y'
print(hasattr(obj,'y'))
print(getattr(obj,'y'))

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

#也可以获得对象的方法
print(hasattr(obj,'power'))
print(getattr(obj,'power'))

fn = getattr(obj,'power') #获取属性power 并赋值到变量fn
print(fn()) #此时的fn()功能与obj.power()是一样的


'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。
hasattr()就派上了用场。
'''
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None




















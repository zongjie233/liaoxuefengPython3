'''
继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。

回忆一下Animal类层次的设计，假设我们要实现以下4种动物：

Dog - 狗狗；
Bat - 蝙蝠；
Parrot - 鹦鹉；
Ostrich - 鸵鸟。
'''
#采用多重继承，主要类层次按照哺乳类和鸟类设计
class Animal():
    pass

#大类
class Mammal(Animal): #哺乳类
    pass

class Bird(Animal): #鸟类
    pass

#各种动物
class Dog(Mammal, RunnableMixIn):

    pass

class Bat(Mammal, FlyableMinIn):
    pass

class Parrot(Bird, FlyableMinIn):
    pass

class Ostrich(Bird, FlyableMinIn):
    pass

#给动物加上Runnable Flyable功能
class RunnableMixIn():
    def run(self):
        print('running...')

class FlyableMixIn():
    def fly(self):
        print('flying...')

#通过多重继承，一个子类就可以同时获得多个父类的所有功能

#Mixln
'''
通常，主线都是单一继承下来的，需要额外功能，通过多重继承可以实现。这种设计称为MixIn
为了更好的看出继承关系，可以把Runnable和Flyable改为RunnableMixIn和FlyableMixIn
MixIn的目的就是给一个类增加多个功能，在设计类的时候，优先考虑通过多重继承来组合多个MixIn的功能。
MixIn只是相当于一个标记，区分出继承的主次，目的是提高代码的可读性
'''


















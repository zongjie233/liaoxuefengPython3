# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student():
    pass

s = Student()
s.name = 'hs'#动态给予属性
print(s.name)

#还可以给实例绑定一个方法
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) #给实例绑定一个方法
s.set_age(21)

print(s.age)
#给实例绑定的方法，对另一个实例是不起作用的，可以给class绑定方法
# Student.set_age = set_age #此语句只是调用方法
Student.set_age=MethodType(set_age,Student) #将方法绑定到类
print(Student.set_age,set_age)
h = Student()
h.set_age(20)
print(h.age)
'''
在动态语言中，上述绑定方法的功能很容易实现，但是在静态语言中难以实现
'''

#使用__slots__
#通过slots可以实现限制class添加属性的功能
class Stu():
    __slots__ = ('name', 'age')

z = Stu()
z.name = 'zfy'
z.age = 21
# z.score = 100 #不在限制范围内，所以会报错

#！！！！__slots__定义的属性支队当前类的实例起作用，对继承的子类是不起作用的


















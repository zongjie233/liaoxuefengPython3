#当需要定义常量时，一个办法是用大写变量通过整数定义
#好处是简单，但是类型为int，并且仍是变量
JAN = 1
FEB = 2
Mar = 3

#更好的方法是为这样的枚举类型定义一个class，每个常量都是class的一个唯一实例。Python提供了Enum类
from  enum import Enum, unique

#获取Month类型的枚举类，可以直接使用Month.Jan来引用一个常量。或者枚举他的所有成员
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 枚举
for name, member in Month.__members__.items():
    print(f'{name} => {member}, {member.value}')#value是自动赋给成员的int常量。默认从1开始

#如果需要精确地控制枚举类型，可以从Enum派生出自定义类：
#枚举类型不可实例化，不可更改
@unique #unique装饰器可以检查 保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(Weekday(1))
for name, member in Weekday.__members__.items():
    print(f'{name} => {member}')

print('-----ex-----')
# ex 把Student的gender属性改造为枚举类型，可以避免使用字符串：
# @unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name

        self.gender = gender

hs = Student('hs',Gender.Male)
print(hs.gender)
print(type(hs.gender))






print('-----------------------------')
#定义枚举

# @unique  # 当用unique装饰后，不能定义相同的成员值
class Color(Enum):

    red = 1
    green = 2
    # red = 3 #定义枚举时，成员名不允许重复
    blue = 1 #但是成员值允许相同，第二个成员的名称会被视为第一个成员的别名，通过该值获取该成员时，只能获取到第一个成员名

print(Color.red)
print(Color.blue)
print(Color.blue is Color.red)
print(Color(1))

print('-----枚举取值-----')
print(Color['red'])#通过成员来获取成员
print(Color(1))#通过成员值来获取成员

member = Color.red
#每个成员都有名称属性和值属性
print(member.name)
print(member.value)

#如果有值重复的成员，只获取重复的第一个成员
for color in Color:
    print(color)

#特殊属性__members__是一个将名称映射到成员的有序字典，也可以通过他完成遍历：
for color in Color.__members__.items():
    print(color)

print('------枚举比较------')
#枚举的成员可以通过is同一性比较或者通过==等值比较
print(Color.red is Color.red)
print(Color.red == Color.red)

print(Color.blue == Color.red)
print(Color.red != Color.red)

#不能进行大小比较
# print(Color.red > Color.red)

print('-----扩展枚举-----')
from enum import IntEnum
#IntEnum是Enum的扩展，不同类型的整数枚举也可以互相比较
class Shape(IntEnum):
    circle = 1
    square = 2

class Request(IntEnum):
    post = 1
    get = 2

print(Shape.circle == 1)
print(Shape.circle < 1)
print(Shape.circle < Request.post)
'''
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
每个对象都拥有相同的方法，但各自的数据可能不同。
'''
# class Student(object):
#     pass

#变量指向一个实例，后边为内存地址，每个object的地址都不一样。Student本身则是一个类
# hs = Student()
# print(hs)
# # 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
# hs.name = 'huang shang'
# print(hs.name)

'''
类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的
时候，就把name，score等属性绑上去：
'''
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# hs = Student('hs',100)
# print(hs.name)
# print(hs.score)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self

# 数据封装
'''
面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，比如
打印一个学生的成绩：
'''
# def print_score(std):
#     print(f'{std.name} {std.score}')

# print_score(hs)

'''
既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问
可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
'''
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'{self.name} {self.score}')

    #可以直接增加新的方法
    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return "C"

hs = Student('huangshang', 100)
hs.print_score()
print(hs.get_grade())

#直接添加自定义属性，不用更改class的格局
hs.appearance = 'handsome'
print(hs.appearance)
# 这样做的好处我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被
# “封装”起来了，调用很容易，但却不用知道内部实现的细节。


# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

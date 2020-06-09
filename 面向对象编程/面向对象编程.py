# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

#为了表示学生的成绩，面向过程的程序可以用一个dict表示
std1 = {'name':'hs','score':100}
std1 = {'name':'zyy','score':90}

#处理学生成绩可以通过函数实现，比如打印学生的成绩
def print_score(std):
    print(f"{std['name']} {std['score']}")

'''
面向对象的设计思想时，首选思考的不是程序的执行流程，而是student这种数据类型应该被视为一个对象，这个对象拥有name score两个属性，如果打
印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。

'''
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'{self.name} {self.score}')

# 面向对象的设计思想是抽象出Class，根据Class创建Instance。
# # 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
''' __init__ 方法的主要作用,就是初始化你的属性,这些属性,在上帝初始化你的时候就要赋予给你,比如zhangsan = Person(170,29,50)这时上帝就把你
# 创造出来了，也就是实例化了你，
'''


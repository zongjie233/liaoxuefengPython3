'''
定义一个class时，可以从某个现有的class继承，新的class称为子类(Subclass)，被继承的称为基类，父类
'''
class Animal():
    def run(self):
        print("Animal is running...")

#编写dog，cat类是可以直接继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class car():
    def run(self):
        print('car is running...')
class Stone():
    pass

class Husky(Dog):
    pass


#继承会使的子类获得父类的全部功能。

'''
当子类和父类都存在相同的run()方法时，子类的run覆盖了父类的run，这样就获得了继承的好处 多态
'''
#当定义一个class的时候，实际上就定义了一种数据类型

# def run_twice(animal): #对于此方法，不一定要传入animal类，任何带有run方法的类都可以传入并运行
#     animal.run()
#
# run_twice(Cat())
# run_twice(car())
# run_twice(Stone())
'''
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
'''



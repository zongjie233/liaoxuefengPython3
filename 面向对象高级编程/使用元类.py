from hello import Hello
#当解释器载入hello模块时，就会意思执行该模块的代码，执行结果就是动态创建出一个Hello的class对象

h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#type()函数既可以返回一个对象的类型，又可以创建出新的类型。
#eg 用type()函数创建出Hello类。
def fn(self, name = 'world'):#先定义函数
    print(f'Hello {name}')

Hello = type('Hello',(),dict(hello = fn)) #创建Hello class

h1 = Hello()
h1.hello()
'''
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
'''

#metaclass 元类
'''
可以使用metaclass 控制类的创建行为
先定义metaclass，就可以创建类，最后创建实例
'''












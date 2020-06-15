#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义，而是动态创建的
class Hello():
    def hello(self, name = 'world'):
        print(f'Hello {name}')

print(type(Hello))
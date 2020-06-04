#通过变量也能调用该函数
def now():
    print('2020-06-04')

f = now
f()

#函数对象有一个__name__属性，可以看到函数的名字
print(now.__name__)
print(f.__name__)

#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def long(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper()
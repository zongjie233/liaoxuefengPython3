#通过变量也能调用该函数
# def now():
#     print('2020-06-04')

# f = now
# f()

# #函数对象有一个__name__属性，可以看到函数的名字
# print(now.__name__)
# print(f.__name__)

#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     #返回的是函数本身，而不是运行的结果
#     return wrapper
# #借助@语法，将decorator置于函数的定义出
# @log
# def now():
#     print('2020-06-05')
#
# now()
#相当于执行了语句 now = long(now)
'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''
#如果decorator函数本身需要传入参数，就需要编写一个高阶函数，
#eg：定义log文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print(f'{text},{func.__name__}')
            return  func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
#相当于运行了now = long('execute')(now)
def now():
    print('2020-06-05')
now()
#经过装饰的函数，__name__变成了’wrapper‘
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
print(now.__name__)

#完整的decorator的写法如下
# 住在定义wrapper()的前面加上@functools.wraps(func)
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(f'call {func.__name__}')
        return func(*args, **kw)
    return wrapper

#带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{text} {func.__name__}')
            return func(*args,**kwargs)
        return wrapper
    return decorator

#ex 设计一个decorator，作用于任何函数，并打印该函数的执行时间
import time
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        op = fn(*args, **kwargs)
        t2 = time.time()
        print(f'{t2-t1}')
        return op
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
fast(6,6)









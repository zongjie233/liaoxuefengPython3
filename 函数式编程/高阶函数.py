#变量可以指向函数
f = abs
print(f(-10))

#函数名也是变量，可以通过import builtins; builtins.abs = 10 修改abs对应的值

#传入函数
#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
    return f(x) + f(y)
print(add(-5,-6,f))


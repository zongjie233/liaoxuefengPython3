#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

#可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#当不需要立刻求和，而是在后面的代码中根据需要进行计算时，可以不返回求和结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#调用lazy_sum()时，返回的是秋和函数
#当调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
a = lazy_sum(1,2,3,4)
print(a)

#闭包
'''
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
'''
#返回的函数没有立刻执行，而是知道调用fn()之后才会执行
#eg
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
#返回结果都为9
print(f1())
print(f2())
print(f3())
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量


#如果一定要引用循环变量，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

#ex利用闭包返回一个计数器函数，每次调用返回递增整数
def createCounter():
#返回函数不要引用任何循环变量，或者后续会发生变化的变量。这里创建列表，本质上是传递的地址
    l1 = [0]
    def counter():
        l1[0] += 1
        return l1[0]
    return counter

A = createCounter()
B = createCounter()
print(A())
print(A())
print(A)




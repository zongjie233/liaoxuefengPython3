#generator
#创建方法1
L = [x * x for x in range(10)]
print(L)
#将[]改为()即可
g = (x * x for x in range(10))
print(g)

#通过next()函数来获取generator的下一个返回值,但正确方法应该是使用for循环
for n in g:
    print(n)

#输出斐波拉契数列前n项
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'

fib(10)

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通的函数，而是一个generator
def fib_generator(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'
f = fib_generator(10)
print(f)
#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print('step1')
    yield
    print('step2')
    yield
    print('step3')
    yield

#调用generator时，首先要生成一个generator对象，然后用next()函数获取下一个返回值
a = odd()
next(a)
next(a)
next(a)

#用for循环调用generator时，拿不到return语句中的返回值，如果想要拿回返回值必须捕获StopIteration
g = fib_generator(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('return value:', e.value)
        break

#杨辉三角形
#使用错位相加的方法
def triangles():
    l = [1]
    s =[]
    while True:
        yield l
        l = [1] + s + [1]
        for i in range(len(l)-1):
            s.append(l[i] + l[i+1])

b = triangles()
print(next(b))
print(next(b))
print(next(b))
print(next(b))






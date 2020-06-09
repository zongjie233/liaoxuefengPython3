#lambda表示匿名函数。只能有一个表达式，不用写return，返回值便是该表达式的结果
#eg
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8])))
'''
这里的lambda实际上就是
def f(x):
    return x * x
    
匿名函数也是一个函数对象，可以吧函数赋值给一个变量，利用变量调用函数
'''
# eg
f = lambda x: x + x
print(f(5))

#同样可以吧匿名函数作为返回值返回
def build(x, y):
    return lambda: x + x - y + y

# ex 请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

L_lambda = list(filter(lambda x: x % 2 == 1,range(1, 20)))
print(L)







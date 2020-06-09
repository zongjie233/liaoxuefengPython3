import functools
#functools 模块中的 偏函数功能(Partial function)
#int()函数可以吧字符串转换为整数，默认按十进制转换
print(int('123456'))

#int()函数提供额外的base参数，默认值为10，可以做N进制的转换
print(int('123456', base = 8))
print(int('123456', base = 16))

#如果要转换大量的二进制字符串，每次都要传入int(x, base = 2)很麻烦，可以定义一个int2（）函数
def int2(x, base = 2):
    return int(x, base)
print(int2('100000'))
#int2()函数只是吧base的默认值设为2.也可以在函数调用时进行更改

#创建偏函数时，实际上可以接受函数对象，*args，**kw这三个参数

#实际上固定了关键字参数base
int2 = functools.partial(int, base = 2)
#相当于kw = {'base' : 2}
# int('10010', **kw)

# 当传入：
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
# 相当于：
args = (10, 5, 6, 7)
max(*args)
# 结果为10。

#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


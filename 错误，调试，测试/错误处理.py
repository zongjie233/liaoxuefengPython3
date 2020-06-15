'''
在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常
常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。
用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错
'''

#try
'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
'''
# try:
#     print('try...')
#     r = 10 / 0
#     print(f'result: {r}')
# except ZeroDivisionError as e:
#     print(f'except:{e}')
# finally:
#     print('finally...')
# print('END')
#当错误发生时，后续语句不会被执行，except由于捕获到错误，执行语句，最后执行finally

# 可以有多个except来捕获不同类型的错误：
# try:
#     print('try...')
#     r = 10 / int('2')
#     print(f'result:{r}')
# except ValueError as e:
#     print(f'ValueError:{e}')
# except ZeroDivisionError as e:
#     print(f'ZeroDivisionError:{e}')
# else:
#     print('no error')
# finally:
#     print('finally..')
# print('END')

#try可以跨越多层调用。
# 函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理：
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
#
# main()

#记录错误
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# main()
print('END')#即使是出现错误,再打印出错误信息之后,后续代码依然会被执行,

'''
因为错误是class，捕获一个错误就是捕获到该class的一个实例。
Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
'''
#根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# class FooError(ValueError):
#     pass
#
# def fo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError(f'invalid value {s}')
#     return 10 / n

# fo('0')
'''
捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比
一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
'''


# ex运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()













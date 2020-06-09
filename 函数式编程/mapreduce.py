#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8])
#查看一个map对象需要list方法
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))

#map作为高阶函数，将运算规则进行抽象。


#将list中的数字全部转化为字符串
print(list(map(str,[1, 2, 3, 4])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。

#将序列变成整数
from functools import  reduce
def fn(x,y):
    return x * 10 + y

print(reduce(fn,[1, 2, 4, 5]))

#将str转化为int
def strtoint(s):
    def fn(x,y):
        return x * 10 + y

    def chartonum(s):
        num = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9

        }
        return num[s]

    return reduce(fn,map(chartonum,s))

print(strtoint('12345'))

#lambda函数简化
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9

        }
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num(), s))

#ex：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    namelow = name[1:].lower()
    nameupp = name[0].upper()
    return nameupp + namelow
print("-测试结果-")
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#ex：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):

    def mutiply(x, y):
        return x * y

    return reduce(mutiply,L)

print("--测试结果--")
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#ex:利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# 标答
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
# # def str2float(s):
# #     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
# #     point = 0
# #     def to_float(f, n):
# #         nonlocal point
# #         if n == -1:
# #             point = 1
# #             return f
# #         if point == 0:
# #             return f * 10 + n
# #         else:
# #             point = point * 10
# #             return f + n / point
# #     return reduce(to_float, nums, 0.0)

# 网答
def str2float(s):
#去除引号
    def k(s):
        digits = {'.': '.', '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    s = list(s)
    result = list(map(k, s))
#确定小数点的位置
    n = result.index('.')
#确定小数点前的整数
    def add1(x, y):
        return x * 10 + y
    float_int = reduce(add1, result[:n])
    m = n +1
#确定小数点后的值
    def add2(q, p):
        return q * 10 + p
    float_flo = 0.1 ** len(result[m:]) * reduce(add2, result[m:])
    return (float_int + float_flo)
print('str2float(\'123.456\') =', str2float('123.456'))







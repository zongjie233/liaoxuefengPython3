#filter()用于过滤序列
#与map()类似，同样接受一个函数和一个序列。不同的是。在传入的函数依次作用于每个元素之后，会根据返回值的True False来决定保留还是丢弃
#eg：在一个list中，删除偶数，保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,3,4,5])))

#删除空字符串,Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#空字符串的bool值为0
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['a','','b'])))

#用filter求素数，埃氏筛法
# 首先，列出从2开始的所有自然数，构造一个序列：
#
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 不断筛下去，就可以得到所有的素数。

#python实现
#先构造一个从3开始的奇数数列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n



#然后定义一个筛选函数
def _not_divisible(n):
    return lambda x : x % n > 0

#最后定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break






#回数是指从左向右读和从右向左读都是一样的数.用filter()筛选出回数：
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print(list(filter(is_palindrome,range(1,100))))





#测试驱动开发（TDD：Test-Driven Development)。单元测试是用来对一个模块，一个函数或者一个类来进行正确性检验的测试工作
'''
比如对函数abs()，我们可以编写出以下几个测试用例：

输入正数，比如1、1.2、0.99，期待返回值与输入相同；

输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

输入0，期待返回0；

输入非数值类型，比如None、[]、{}，期待抛出TypeError。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
'''

'''
单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影

响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。
'''



# d = Dict(a = 1, b = 2)
# print(d['a'])
# print(d.a)

#引入自带的unittest模块，编写mydict_test.py
import unittest
























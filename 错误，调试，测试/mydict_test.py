# 为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value') #断言函数返回的结果与'value'相等

    def test_keyerror(self):
        d = Dict()
        #期待抛出指定类型的Error
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
'''
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
'''

'''
setUp tearDown
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码
'''
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score > 100:
#              raise ValueError
#         elif self.score >= 80:
#              return 'A'
#         elif self.score >= 60:
#             return 'B'
#         elif self.score >= 0:
#             return 'C'
#         else:
#             raise ValueError





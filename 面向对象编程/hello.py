#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#前两行为标准注释。第一行注释可以让这个文件直接在unix、linux、mac上运行，第二个注释表示py文件
# 本身使用标准utf-8编码；

#hello 模块
#文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

'a test module'

#使用__author__变量将作者写进去
__author__ = 'Coach huang'


import sys

#argv至少有一个元素，因为第一个参数永远是该.py文件的名称
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print(f"hello {args[1]}")
    else:
        print("Too many arguments!")

if __name__=='__main__':
    test()
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
'''
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也
可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

'''
#断言, 凡是可以用print()来辅助查看的地方 都可以用断言(assert)来替代
# def foo(s):
#     n = int(s)
#     # assert意思是，表达式n!=0应该是True，否则根据程序运行的逻辑，后面的代码就会出错，如果断言失败就会抛出AssertionError
#     assert n != 0, 'n is zero'
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

#python解释器可以通过-O参数来关闭assert，关闭之后assert语句可以当成pass看待

# logging
'''
logging不会抛出错误，而且可以输出到文件,允许指定记录信息的级别
通过简单的配置，一条语句可以同时输出到不用的地方，比如console和文件
'''
# import logging
#
# s = '0'
# n = int(s)
# logging.info(f'n = {n}')
# print(10 / n)

#pdb
'''
启动python的调试器，让程序以单步方式运行，可以随时查看运行状态
'''

# pdb.set_trace()
'''
这个方法也是用pdb，但是不需要但不执行，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断电
'''
import pdb

s = '0'
n = int(s)
pdb.set_trace() #运行到这里就会自动暂停，可以用命令c继续执行
print(10 / n)











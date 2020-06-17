import os
print(os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

print(os.environ) #查看操作系统中定义的环境变量

# 要获取某个变量的值，可以调用os.envision.get('key')
print(os.environ.get('PATH'))

#查看当前目录的绝对路径
print(os.path.abspath('.'))

#在某个目录下创建一个新目录,在创建之前需要把新目录的完整路径表示出来，使用os.path.join()
# print(os.path.join('D:\\PythonProject\\liaoxuefengPython3\\IO编程','testdir'))
# os.mkdir('D:\\PythonProject\\liaoxuefengPython3\\IO编程\\testdir')
# os.rmdir('D:\\PythonProject\\liaoxuefengPython3\\IO编程\\testdir')

#要拆分路径时，不要拆字符串，而是通过os.path.split()函数。可以吧一个路径拆分为两部分，后一部分总是最后级别的目录活着文件名：
print(os.path.split('D:\\PythonProject\\liaoxuefengPython3\\IO编程\\test.txt'))

# os.path.splitext()可以直接得到文件扩展名。这些函数只会对路径进行拆分操作
print(os.path.splitext('D:\\PythonProject\\liaoxuefengPython3\\IO编程\\test.txt'))

#对文件重命名
# os.rename('test.txt','test.py')
#删掉文件：
# os.remove('test.py')

#os模块中没有copyfile()函数，可以使用shutil模块中找到，可以看作是os模块的补充

#利用Python的特性来过滤文件，eg列出当前目录下的所有目录,或者所有.py
print(os.getcwd())
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])












'''
数据读写不一定是文件，也可以在内存中读写。stringIo顾名思义就是在内存中读写str
需要创建一个stringIO，像文件一样写入
'''
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world'))

print(f.getvalue()) #getvalue()方法用于获得写入后的str

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取:
f = StringIO('Hello!\nHi\nGoodBye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#BytesIO,StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8'))) #这里写入的不是str，而是经过UTF-8编码的bytes
print(f.getvalue())

#与StringIO类似，可以用一个bytes初始化BytesIO，然后像读文件一样读取：
f = BytesIO(b'82385')
print(f.read())





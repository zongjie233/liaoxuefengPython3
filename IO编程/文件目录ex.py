# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
# 查找文件名包含s的文件
import os
def Get_Path(s):
    Q, result = ['.'], []             # Q是目录队列
    while Q:                          # 队列不为空
        p = Q[0]                      # 取出队头
        Q = Q[1:]                     # 弹出队头
        for x in os.listdir(p):       # 遍历当前目录下文件
            if os.path.isdir(x):      # 如果这个是目录
                Q.append(x)           # 加入队列
            elif os.path.isfile(x) and (s in x):   # 如果是文件并且文件名包含s
                result.append(os.path.abspath(x))  # 符合要求的文件名
    return result

print(Get_Path('test'))
print(os.listdir('.'))

def find_file(s):
    Q, result = ['.'], []
    while Q:
        p = Q[0]
        Q = Q[1:]
        for x in os.listdir(p):
            if os.path.isdir():
                Q.append(x)
            elif os.path.isfile(x) and (s in x):
                result.append(os.path.abspath(x))
    return result
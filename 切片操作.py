# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if s[0] == " ":
        return s[1:]

    elif s[-1] == " ":
        return s[:-1]
    else:
        return s
    print(s)
print(trim(' hello'))

#字符串为不可变对象
s = ' hello world'

print(s.split(" "))
print(s)
    

    

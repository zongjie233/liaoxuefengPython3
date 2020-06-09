# Python内置的sorted()函数可以对list进行排序
print(sorted([1,4,6,2,6]))

#sorted()函数可以接受一个key函数来实现自定义的排序，eg 按照绝对值大小排序
print(sorted([2,5,7,-3,-8,-5], key = abs))

#实现 忽略大小写的排序
print(sorted(['boy','apple','Ce'], key=str.lower))
#反向排序，只需要传入第三个参数
print(sorted(['boy','apple','Ce'], key=str.lower,reverse = True))

#ex L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 用sorted()对上述列表分别按照名字,成绩排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[1])

def by_name(t):
    return sorted(t,key = lambda student:student[0])

def by_score(t):
    return sorted(t,key = lambda student:student[1],reverse=True)

print(by_name(L))
print(by_score(L))


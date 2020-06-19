#在程序运行的过程中，所有的变量都是在内存中，比如定义一个dict：


'''
变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。
'''
# import pickle
# d = dict(name = 'hs', age = 20, score = 100)
# print(pickle.dumps(d))

#pickle.dumps()可以把任意对象序列化称为一个bytes，然后就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个
# file-like object
# f = open('test.txt','wb') #此时的文件内容为乱码。这些就是python保存的对象内部信息
# pickle.dump(d,f)
# f.close()

'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个
file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
'''
# f = open('test.txt','rb') #此时的文件内容为乱码。这些就是python保存的对象内部信息
# d = pickle.load(f)
# f.close()
# print(d)

#json
'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
'''

'''
JSON类型	      Python类型
{}	            dict
[]	            list
"string"	    str
1234.56	    int或float
true/false	True/False`
null	        None
'''
import json
d = dict(name = 'Bob', age = 20)
print(json.dumps(d)) #dumps()方法返回一个str。dump()方法可以直接把json写入一个file-like Object

#json反序列化为python对象
json_str = '{"name": "Bob", "age": 20}'
print(json.loads(json_str))

'''
JSON进阶
Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
'''
class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score



# 改变可选参数，定制json序列化。为Student写一个转换函数，再将函数传进去即可
def student2dict(s):
    return {
        'name': s.name,
        'age' : s.age,
        'score' : s.score
        }


a = Student('hs', 20, 100)
print(json.dumps(a, default=student2dict)) #程序运行报错，因为Student对象不是一个可序列化为json的对象

#上述方法不通用，如果换为其他实例便不会起作用。可以进行如下操作
# print(json.dumps(s, default=lambda obj: obj.__dict__)) #将任意class的实例变为dict


# JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# ex对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
# 如果ensure_ascii为True(默认值)，则输出保证将所有输入的非ASCII字符转义。如果确保ensure_ascii为False，这些字符将原样输出。
print(json.dumps(obj, ensure_ascii=False))


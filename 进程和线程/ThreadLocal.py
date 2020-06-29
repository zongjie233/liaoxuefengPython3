'''
一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
'''
#局部变量在函数调用的时候传递起来很麻烦
'''
def process_student(name):
    std = Student(name)
    #std是局部变量，但是每个函数都需要，所以必须传进去
    do_task_1(std)
    do_task_2(std)
    
def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
'''

#用一个全局dict存放所有的student对象，然后以thread自身作为key获得线程对应的student对象
# global_dict = {}
#
# def std_thread(name):
#     std = Student(name)
#     # 将std放到全局变量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
#
# def do_task_1():
#     # 不传入std，而是根据当前线程查找
#     std = global_dict[threading.current_thread()]
#
#
# def do_task_2():
#     # 不传入std，而是根据当前线程查找
#     std = global_dict[threading.current_thread()]

#THreadLocal可以不用查找dict，自动完成这个过程
import threading
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print(f'hello, {std} (in {threading.current_thread().name})')

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Hs',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('zfy',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但是互不影响

全局变量local_school是一个dict，可以绑定其他变量。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
'''

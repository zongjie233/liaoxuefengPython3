'''
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，
我们只需要使用threading这个高级模块。
'''
#启动一个线程就是将一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading

#新线程执行的代码
# def loop():
#     print(f'thread {threading.current_thread().name} is running...')
#     n = 0
#     while n < 5:
#         n += 1
#         print(f'thread {threading.current_thread().name} >>> {n}')
#         time.sleep(1)
#     print(f'thread {threading.current_thread().name} ended.')
#
# print(f'thread {threading.current_thread().name}')
# t = threading.Thread(target=loop, name='LoopThread') #创建Thread实例，传入函数
# t.start()
# t.join()
# print(f'thread {threading.current_thread().name} ended')
'''
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定,
我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''

'''
Lock
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改

下述代码正常运行时 结果balance = 0，但线程是交替运行的，所以交替运行多次可能会出错
原因是修改balance需要多条语句，而执行这些语句时，线程可能终端，从而导致多个线程把同一个对象的内容改乱了，两个线程同时一存一取，
就可能导致余额不对。
'''
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock() #创建🔒

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

'''
必须确保一个线程在修改balance的时候，别的线程一定不能改动
要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等
待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
创建一个🔒是通过threading.Lock()来实现的
'''
'''
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

'''

'''
Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线
程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
'''
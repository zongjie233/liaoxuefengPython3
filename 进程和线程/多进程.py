'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动
把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用
getppid()就可以拿到父进程的ID。
'''

import os
# print(f'Process {os.getpid()} start')

# pid = os.fork() #只有Unix Linux Mac可运行

#multiprocessing
#multiprocessing模块提供了一个Process类来代表一个进程对象。
# from multiprocessing import Process
# import os
#
# #子进程要执行的代码
# def run_proc(name):
#     print(f'Run child process {name} ({os.getpid()})')
#
# if __name__ == '__main__':
#     print(f'Parent process {os.getpid()}')
#     p = Process(target=run_proc, args = ('test',)) #创建实例
#     print('Child process will start.')
#     p.start()
#     p.join() #join方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#     print('Child process end.')

#启动大量的子进程时，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

# def long_time_task(name):
#     print(f'Run task {name} ({os.getpid()})')
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print(f'Task {name} runs {(end - start)}')
#
# if __name__ == '__main__':
#     print(f'Parent process {os.getpid()}')
#     p = Pool(15)
#     for i in range(15):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
# #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#     p.close()
#     p.join()
#     print('All subprocesses done.')


'''
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
# import subprocess
# print('$ nslookup www.baidu.com')
# r = subprocess.call(['nslookup', 'www.baidu.com'])
# print(f'Exit code: {r}')

#如果子进程还需要输入，则可以通过communicate()方法输入：
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

'''
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print(f'Process to write: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'Put {value} to queue...')
        q.put(value)
        time.sleep(random.random())

def read(q):
    print(f'Process to read: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'Get {value} from quene.')

if __name__ == '__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入：
    pw.start()
    #启动子进程pr, 读取：
    pr.start()
    #等待pw结束
    pw.join()
    #pr为死循环，只能强行停止
    pr.terminate()


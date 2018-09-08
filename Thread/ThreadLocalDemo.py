
'一个关于ThreadLocal的小DEMO，ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰'

import threading

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

# 创建一个全局的local对象
local_school = threading.local()


def process_student():
    '''
    获取当前线程关联的student
    '''
    stu = local_school.student
    # 这里的threading.current_thread().name，name是个属性，不是方法
    # %后面多个对应的时候要加()
    print('Hello,%s in %s' % (stu, threading.current_thread().name))


def process_thread(name):
    '''
    绑定ThreadLocal的student
    '''
    local_school.student = name
    process_student()


# 这里需要给线程一个名字
thread_one = threading.Thread(
    target=process_thread, args=('Thread_One',), name='Thread_One')
thread_two = threading.Thread(
    target=process_thread, args=('Thread_Two',), name='Thread_Two')

thread_one.start()
thread_two.start()
thread_one.join()
thread_two.join()

# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

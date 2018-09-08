# 如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行
# 现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。
# 怎么用分布式进程实现？
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

'服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务'

import random
import time
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列
task_queue = queue.Queue()

# 接收结果的队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


# 加入if name == main 判断. 第二点是windows平台对于python多进程实现的要求.主要为了防止循环import
if __name__ == '__main__':
    freeze_support()
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象
    # 在win10环境下，pickle模块不能序列化lambda函数，所以需要自定义task_queue和result_queue
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定5000端口，设置验证码为abc
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    # 通过网络访问Queue对象，至于这里为什么会报红，无所谓
    task = manager.get_task_queue()
    # print(task)
    result = manager.get_result_queue()
    # print(result)

    # 往里面放一些任务
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列中读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result %d:%s' % ((i + 1), r))

    # 关闭
    manager.shutdown()
    print('master exit.')

# 先启动task_master.py服务进程
# task_master.py进程发送完任务后，开始等待result队列的结果。现在启动task_worker.py进程
# task_worker.py进程结束，在task_master.py进程中会继续打印出结果

import time
import queue

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接服务器，即运行task_master的机器
server_add = '127.0.0.1'
print('Connect to server %s...' % server_add)

# 端口和验证码要和master一样
manager = QueueManager(address=(server_add, 5000), authkey=b'abc')
# 从网络连接
manager.connect()

# 获取Queue对象
task = manager.get_task_queue()
# print(task)
result = manager.get_result_queue()
# print(result)

# 从task队列取任务，处理后将结果放入result
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        # 这里的停顿也要久一点，不然会被拒绝访问
        time.sleep(2)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

print('worker exit.')

'进程间通信'

from multiprocessing import Process, Queue
import os
import time
import random


def write(q):
    '''
    写数据进程执行的代码
    '''
    print("Process to write: %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    '''
    读数据进程执行的代码
    '''
    print("Process to read: %s" % os.getpid())
    while True:
        # 至于这里为什么是get(True)
        value = q.get(True)
        print("Get %s from queue." % value)


if __name__ == "__main__":
    # 父进程创建Queue，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法结束，只能强制终止
    pr.terminate()

import time
import threading

'玩一下多线程'


def loop():
    '''
    新线程执行的代码
    '''
    # current_thread()永远返回当前线程的实例
    print('Thread %s is running.' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)


# 任何进程默认就会启动一个线程
print('Thread %s is running.' % threading.current_thread().name)
# 子线程的名字在创建时指定
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)

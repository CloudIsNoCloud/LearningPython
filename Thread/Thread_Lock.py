import time
import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    # global关键字，调用为全局变量，没用这个关键字不能修改值
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    i = 0
    while i < 10000:
        # 先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()
            i += 1


thread_one = threading.Thread(target=run_thread, args=(5,))
thread_two = threading.Thread(target=run_thread, args=(8,))
thread_one.start()
thread_two.start()
thread_one.join()
thread_two.join()

print(balance)

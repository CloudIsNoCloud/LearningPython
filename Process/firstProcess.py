'用来玩的进程'

from multiprocessing import Process
import os
# 子进程要执行的代码


def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    # args的参数应该是tuple，只有一个元素的时候尾巴要加,
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    p = Process(target=run_proc, args=("test",))
    print("Child process will start.")

    # 这个进程开启之后自己运行， 在调试控制台看不到它的输出
    # 用start()方法启动，这样创建进程比fork()还要简单。
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()

    print("Child process end.")

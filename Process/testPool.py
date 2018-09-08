'玩一下进程池'

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print("Run task %s (%s)." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s runs %0.2f s." % (name, (end-start)))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
    p = Pool(5)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    print("Waithing for all subprocess done...")
    p.close()
    p.join()
    print("All subprocess done.")

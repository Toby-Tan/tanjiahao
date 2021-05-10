# 进程池pool
# 进程池必须使用Manager下的Queue
from multiprocessing import Pool, Manager
# from multiprocessing import Queue
import os
import time


def work_1(queue):
    print('任务:{}----进程id:{}'.format(queue.get(), os.getpid()))
    # time.sleep(0.5)


if __name__ == '__main__':
    queue = Manager().Queue()
    num = 10
    for i in range(num):
        i += 1
        queue.put(i)

    # 创建进程池
    pool = Pool(5)
    while queue.qsize() > 0:
    # for i in range(num):
        pool.apply_async(work_1, (queue,))
        time.sleep(0.5)

    pool.close()
    pool.join()

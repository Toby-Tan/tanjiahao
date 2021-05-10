# 进程

# from queue import Queue
# 进程间相互通讯必须使用进程包里的Queue
from multiprocessing import Process, Queue
import time

count = 0


def work_1(a):
    global count
    while a.qsize() > 0:
        count += 1
        print('任务一第{}次执行---执行次数{}'.format(a.get(), count))
        time.sleep(0.5)


def work_2(a):
    global count
    while a.qsize() > 0:
        count += 1
        print('任务二第{}次执行---执行次数{}'.format(a.get(), count))
        time.sleep(0.5)


if __name__ == '__main__':
    a = Queue()
    for i in range(10):
        i += 1
        a.put(i)
    p1 = Process(target=work_1, args=(a,))
    p2 = Process(target=work_2, args=(a,))
    p1.start()
    p2.start()

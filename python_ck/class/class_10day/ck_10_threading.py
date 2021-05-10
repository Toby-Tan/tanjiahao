# 同步与异步

# 并发与并行、串行

# threading模块

import threading
import time


def fun1():
    for i in range(5):
        time.sleep(1)
        print('---执行方法1---')


def fun2():
    for i in range(6):
        time.sleep(1)
        print('---执行方法2---')


def main_time():
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    start_time = time.time()
    t1.start()
    print(threading.current_thread())  # 返回当前执行的线程
    t2.start()
    # print(threading.enumerate())  # 返回正在运行的所有线程对象list，启动后，结束前，不包括启动前和终止后的线程
    # print(threading.active_count())  # 返回正在运行的线程数量

    # t1.join(4)
    t2.join()  # join()方法：t2执行完成后执行主线程

    end_time = time.time()
    print('总耗时：', end_time - start_time)


main_time()

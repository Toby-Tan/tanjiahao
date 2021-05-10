# 多线程全局变量
# 如果多个线程同时对一个全局变量操作，会出现资源竞争问题，从而会导致数据结果错误

import threading
import time

a = 100


def fun1():
    global a
    for i in range(1000000):
        a += 1
    print(a)


def fun2():
    global a
    for i in range(1000000):
        a += 1
    print(a)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
t2.start()
t1.join()
t2.join()

print(a)

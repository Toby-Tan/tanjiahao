# 多线程全局变量
# 如果多个线程同时对一个全局变量操作，会出现资源竞争问题，从而会导致数据结果错误
# Lock()互斥锁



import threading
import time

a = 0
m_lock_1 = threading.Lock()
m_lock_2 = threading.Lock()


def fun1():
    global a
    for i in range(1000000):
        m_lock_1.acquire()
        # m_lock_2.acquire()
        a += 1
        # m_lock_2.release()
        m_lock_1.release()
    print(a)


def fun2():
    global a
    for i in range(1000000):
        m_lock_1.acquire()
        # m_lock_1.acquire()
        a += 1
        # m_lock_1.release()
        m_lock_1.release()
    print(a)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
s_time = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
e_time = time.time()
print(a)
print('耗时：', e_time - s_time)

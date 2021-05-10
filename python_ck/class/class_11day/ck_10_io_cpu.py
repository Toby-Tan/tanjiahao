import threading
import time
import requests

a = 100


def fun3():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    for i in range(10):
        requests.get('http://www.baidu.com', headers=headers)


def fun4():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    for i in range(10):
        requests.get('http://www.baidu.com', headers=headers)


def fun1():
    global a
    for i in range(100000000):
        a += 1


def fun2():
    global a
    for i in range(100000000):
        a += 1

s_time = time.time()
# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)

# t3 = threading.Thread(target=fun3)
# t4 = threading.Thread(target=fun4)


# fun1()
# fun2()
fun3()
fun4()

# t3.start()
# t4.start()
# t3.join()
# t4.join()

# t1.start()
# t2.start()
# t1.join()
# t2.join()
e_time = time.time()
print(a)
print('耗时：', e_time - s_time)

"""
cpu密集型：在多重程序系统中，大部份时间用来做计算、逻辑判断等CPU动作的程序称之CPU bound
单线程跑
200000100
耗时： 13.528753995895386
多线程跑
125429390
耗时： 11.381195068359375
结论：

I/O密集型：I/O bound的程序一般在达到性能极限时，CPU占用率仍然较低
单线程跑
100
耗时： 3.9072813987731934
多线程跑
100
耗时： 1.997162103652954
结论：
"""

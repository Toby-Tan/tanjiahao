import threading
import time
import requests
from queue import Queue

acount = 0




# def fun4():
#     global acount
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
#     }
#     for i in range(1000):
#         requests.get('http://127.0.0.1:5000/', headers=headers)
#         acount += 1
#         print('{}次请求'.format(acount))

def fun3():
    global acount
    while q.qsize() > 0:
        url = q.get()
        requests.get(url=url)
        acount += 1
    print('{}次请求'.format(acount))


q = Queue()
for i in range(1000):
    q.put('http://127.0.0.1:5000/')

if __name__ == '__main__':
    s_time = time.time()
    t1 = threading.Thread(target=fun3)
    t2 = threading.Thread(target=fun3)
    t3 = threading.Thread(target=fun3)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    e_time = time.time()
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
# 0.7021236419677734

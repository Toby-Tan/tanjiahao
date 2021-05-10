# 进程

# from queue import Queue
# 进程间相互通讯必须使用进程包里的Queue
from multiprocessing import Process, Pool, Manager
import time
import requests


# def fun4():
#     global acount
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
#     }
#     for i in range(10):
#         requests.get('http://cas.kt3.pagoda.com.cn/login', headers=headers)
#         acount += 1
#         print('{}次请求'.format(acount))

acount = 0

def fun3(q):
    global acount
    while q.qsize() > 0:
        url = q.get()
        requests.get(url=url)
        acount += 1
    print('{}次请求'.format(acount))


if __name__ == '__main__':
    q = Manager().Queue()
    for i in range(1000):
        q.put('http://127.0.0.1:5000/')
    # print(q.qsize())
    pool = Pool(3)
    s_time = time.time()
    for i in range(3):
        # 异步非阻塞，不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
        pool.apply_async(fun3, args=(q,))
    pool.close()
    pool.join()
    e_time = time.time()
    print('耗时：', e_time - s_time)

# 1.0141324996948242

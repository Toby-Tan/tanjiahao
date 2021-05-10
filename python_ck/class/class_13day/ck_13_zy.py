"""
10000个请求，开启两个进程，进程中开启3个线程，线程中开启5个协程来处理
协程补丁：
monkey.patch_all()
"""
import time
from multiprocessing import Process, Queue
import threading
import gevent
import requests


def count_time(func):
    def wrapper(*args, **kwargs):
        print("---开始执行---")
        s_time = time.time()
        func(*args, **kwargs)
        e_time = time.time()
        print("---结束执行---")
        print("任务耗时：{}".format(e_time - s_time))

    return wrapper


def process_work(q, qname):
    thr_list = []
    for i in range(1, 4):
        tname = "{}-t{}".format(qname, i)
        print("创建线程{}".format(tname))
        t = threading.Thread(target=thread_work, args=(q, tname))
        t.start()
        thr_list.append(t)
    for i in thr_list:
        i.join()


def thread_work(q, tname):
    gevent_list = []
    for i in range(1, 6):
        gname = "{}-g{}".format(tname, i)
        print("创建协程{}".format(gname))
        g = gevent.spawn(gevent_work, q, gname)
        g.start()
        gevent_list.append(g)
    gevent.joinall(gevent_list)


def gevent_work(q, gname):
    count = 0
    while q.qsize() > 0:
        url = q.get(timeout=0.01)
        requests.get(url=url)
        gevent.sleep(0.001)
        count += 1
    print('协程{}执行了{}个任务'.format(gname, count))


@count_time
def main():
    q = Queue()
    for i in range(10000):
        q.put('http://127.0.0.1:5000')
    print('创建队列，共{}条数据'.format(q.qsize()))
    pro_list = []
    for i in range(1, 3):
        qname = "p{}".format(i)
        print('创建进程{}'.format(qname))
        p = Process(target=process_work, args=(q, qname))
        p.start()
        pro_list.append(p)
    for i in pro_list:
        i.join()


if __name__ == '__main__':
    main()

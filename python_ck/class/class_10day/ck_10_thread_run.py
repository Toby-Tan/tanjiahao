# 重写run()方法

import threading
import requests
import time


class RequestRun(threading.Thread):

    def __init__(self, url):
        self.url = url
        super().__init__()

    # 重写了父类Thread的run方法，然后strat()直接调用了这个方法
    def run(self):
        # time.sleep(1)
        # print('--运行等待--{}'.format(threading.current_thread()))
        res = requests.get(self.url)
        print('--状态码--{}---{}: '.format(res.status_code, threading.current_thread()))


def count():
    s_time = time.time()
    for i in range(5):
        t = RequestRun('https://www.baidu.com')
        t.start()
        t.join()
    e_time = time.time()
    print('耗时：', e_time - s_time)


count()

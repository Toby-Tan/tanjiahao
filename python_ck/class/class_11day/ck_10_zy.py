#

import threading
import time
import requests

count = 0


class ThreadRequests(threading.Thread):
    def run(self):
        global count
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
        for i in range(100):
            requests.get('https://baidu.com', headers=headers)
            count += 1
            print('---Thread-{}--第{}次请求'.format(self.name, i + 1))


# res_li = []
# for i in range(10):
#     thread = ThreadRequests()
#     res_li.append(thread)


def main():
    s_time = time.time()
    res_li = [ThreadRequests() for j in range(10)]
    for i in res_li:
        i.start()
    for i in res_li:
        i.join()
    e_time = time.time()
    print(count)
    print('每个请求平均响应时间：{}'.format((e_time - s_time) / count))


main()

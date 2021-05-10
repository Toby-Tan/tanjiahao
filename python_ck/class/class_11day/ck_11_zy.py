import threading
import time
import queue

# goods = []
goods_queue = queue.Queue()


class Producer(threading.Thread):

    def run(self):
        count = 0
        while True:
            if goods_queue.qsize() < 50:
                for i in range(200):
                    count += 1
                    goods = '生产{}个商品.'.format(count)
                    goods_queue.put(count)
                    print(goods)
            time.sleep(1)


class Consumer(threading.Thread):

    def run(self):
        while True:
            if goods_queue.qsize() >= 10:
                for i in range(3):
                    print('消费{}个商品.'.format(goods_queue.get()))
            else:
                time.sleep(1)

pro_thread = Producer()
pro_thread.start()
# pro_thread.join()

cons = [Consumer() for i in range(5)]
for i in cons:
    i.start()

# print(goods_queue.qsize())

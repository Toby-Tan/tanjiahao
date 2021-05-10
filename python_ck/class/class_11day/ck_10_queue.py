"""
三种队列
1.先入先出
2.后入先出
3.优先级
"""
import queue

# 先入先出
p = queue.Queue(3)
p.put(5)
p.put(3)
p.put(6)
# print(p.get())
# print(p.get())
# print(p.get())

# print(p.qsize())  # 查询队列消息数量
# print(p.full())  # 判断队列是否已满
# print(p.empty())  # 判断队列是否为空
# join：执行完成task_done()才会继续往下执行
# p.task_done()
# p.task_done()
# p.task_done()
# p.join()
# print('继续往下执行')

# 后入先出,方法和先入先出一样
p2 = queue.LifoQueue(3)
p2.put(1)
p2.put(12)
p2.put(123)
print(p2.get())

# 优先级
data = [1, 2, 3]
p3 = queue.PriorityQueue()
p3.put((3, data))
p3.put((1, data))
p3.put((4, data))
p3.put((23, data))
p3.put((6, data))

print(p3.get())
print(p3.get())
print(p3.get())


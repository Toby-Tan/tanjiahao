import time


def time_count(num_test):
    def time_num(*args, **kwargs):
        start_time = time.time()
        print(start_time)
        num_test(*args, **kwargs)
        end_time = time.time()
        print(end_time)
        print('函数运行时间:{:.5f}'.format(end_time - start_time))

    return time_num

@time_count
def num_test():
    li = []
    for i in range(1, 11):
        new_num = i + 1
        li.append(new_num)
    print(li)

num_test()


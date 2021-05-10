import timeit
from collections import namedtuple


def func():
    for i in range(10):
        print(i)


# res2 = timeit.timeit(func, number=100)

# res = timeit.Timer(stmt=func).timeit(100)
# print(res)

# print(res2)
info = namedtuple('info_test', ['name', 'age', 'gender'], )
tu = info('tan', 18, 'nan')
# print(tu.name)
# print(type(tu))

lists = [1, 2, 3, 4, 4, 5, 3, 2, 1, 2, 2, 1, 3, 2]
# lists.reverse()
# print(lists)
li = set(lists)  # list转换成集合去重
print(list(li))  # 再转换成list

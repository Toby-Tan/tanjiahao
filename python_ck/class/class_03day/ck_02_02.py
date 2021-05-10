# 装饰器
# 开放封闭原则

def add_num(a, b):
    print(a + b)


def fun(*args, **kwargs):
    print(*args, **kwargs)


num = (1, 2, 3, 4)
dic = {1: 1, 2: 2}
fun(1, )


# 装饰器装饰类
class Myclass:
    def __init__(self):
        pass

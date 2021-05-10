# 装饰器
# 开放封闭原则
import time


def login(sd):
    def fun():
        username = 'python'
        pw = "111111"
        user = input('请输入账号')
        password = input('请输入密码')
        if user == username and password == pw:
            sd()
        else:
            print('账号或者密码错误')

    return fun


# @login  # @login --> inx = login(index)
# def index():
#     print('网站首页')


# index()


# inx = login(index)
# inx()
def f1(g):
    print("in f1")
    return g


@f1
def f2():
    print("in f2")


@f1
def f3():
    print('in f3')

# f2()
# f2()
# f3()
# print('----')
# f2()
# f3()

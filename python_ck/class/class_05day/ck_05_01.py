# 多个装饰器装饰同一个函数
import time

with open('user.txt', 'r') as f:
    data = eval(f.read())  # 转换成字典


def warpper(func):
    def time_count(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('函数运行时间:{:.5f}'.format(end_time - start_time))
    return time_count


def login_check(func):
    """

    :param func:
    :return:
    """
    def ado(*args, **kwargs):
        while not data['token']:
            print('----登录-----')
            username = input('请输入账号')
            password = input('请输入密码')
            if data['user'] == username and data['pwd'] == password:
                data['token'] = True
                func(*args, **kwargs)
                break
            else:
                print('账号密码错误，请重新输入')

        else:
            func(*args, **kwargs)
    return ado


@login_check
@warpper
def fun_i():
    time.sleep(3)
    print('需要被装饰的函数')


fun_i()

# python内置的3个装饰器


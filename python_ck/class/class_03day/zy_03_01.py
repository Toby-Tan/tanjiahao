# import json
#
with open('user.txt', 'r') as f:
    data = eval(f.read())  # 转换成字典


# def login_check(func):
#     """
#     登录检测token，token为False时跳转登录页面，为True时直接调用后续
#     :param func: 被装饰函数
#     :return: 被装饰函数
#     """
#
#     def login():
#         if data['token']:
#             func()
#         else:
#             while not data['token']:
#                 print('----登录-----')
#                 username = input('请输入账号')
#                 password = input('请输入密码')
#                 if data['user'] == username and data['pwd'] == password:
#                     data['token'] = True
#                     func()
#                     break
#                 else:
#                     print('账号密码错误，请重新输入')
#     return login
#
#
# @login_check
# def index():
#     print('首页')


# index()


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
def index():
    print('-1index1-')


index()

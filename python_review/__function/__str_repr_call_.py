
# 魔术方法

class Myclass(object):

    def __init__(self,name):
        print('__init__被调用')
        self.name = name

    # 当__str__方法不存在时，调用__repr__方法，
    # 都不存在则找父类的__str__->>>__repr__

    # def __str__(self):
    #     print('__str__被调用')
    #     # return object.__str__(self)
    #     return 'aaa'
    def __repr__(self):
        print('__repr__被调用')
        # return object.__repr__(self)
        return 'bbb'

    def __call__(self, *args, **kwargs):
        print('__call__方法被调用')


# a = Myclass('tanjiahao')
# str(a)
# a()

# 类实现装饰器,既可以装饰类，也可以装饰函数，可以接收参数
# 通过call魔术方法实现
class Callbackclass(object):

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('---执行函数前功能---')
        self.func()
        print('---执行函数后功能---')

# 装饰函数
@Callbackclass
def t(a=2,b=3):
    print(a+b)
    print('__t__被调用')

# t()

# 装饰类
@Callbackclass
class MyCase:

    def __init__(self,name='tanjiahao'):
        self.name = name
        print(self.name)

    def te(self):
        print('---类方法被调用--')

# MyCase()
a = Callbackclass(MyCase)
print(a.func)
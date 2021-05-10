# 单例模式
# 1、单例类只能有一个实例。
# 2、单例类必须自己创建自己的唯一实例。
# 3、单例类必须给所有其他对象提供这一实例。


# 通过重写__new__方法实现单例类
class Mytest():
    instance = None  # 设置一个类属性用来记录该类有没有创建过对象

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance


a = Mytest()
b = Mytest()


# print(id(a), id(b))


# 通过装饰器实现单例模式。面试题
def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    __instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
            # __instance[cls] = object.__new__(cls)
        # 将实例对象返回
        return __instance[cls]

    return _singleton


from selenium import webdriver


@singleton
class A():

    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        # self.moblie = moblie
        # print(self.name, self.moblie)


a1 = A('tanjiahao', 15873167367)
a2 = A('1', 11)
print(id(a1), id(a2))


@singleton
class B():
    a = 1


b1 = B()
b2 = B()
print(id(b1), id(b2))

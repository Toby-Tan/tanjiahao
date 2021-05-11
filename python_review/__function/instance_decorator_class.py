# 装饰器实现单例模式

def instance(cls):

    __instance = {}
    def func(*args,**kw):
        if cls in __instance:
            return __instance[cls]
        else:
            __instance[cls] = cls(*args,**kw)
            print(__instance)
            return __instance[cls]
    return func

@instance
class Mytest(object):
    print('--Mytest--调用')

@instance
class Myclass(object):
    print('--Myclass--调用')

a = Mytest()
b = Mytest()
c = Myclass()
d = Myclass()
print(id(b))
print(id(c))
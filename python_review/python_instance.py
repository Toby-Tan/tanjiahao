# 单例模式
class Mytest(object):

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance




t1 = Mytest()
t1.name = 'tanjiahao'
if __name__ == '__main__':
    print(t1.name)
    t2 = Mytest()
    # t2.name = 'toby'
    print(t2.name)
    print(id(t1))
    print(id(t2))
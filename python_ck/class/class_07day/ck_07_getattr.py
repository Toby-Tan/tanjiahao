class Test:
    # def __getattr__(self, item):
    #     # 访问属性时，属性不存在（AttrError）,该方法触发
    #     print('__getattr__被调用')
    #     # object.__getattribute__(self,item)
    #     return 100
    #
    # def __getattribute__(self, item):
    #     # 访问属性时，第一时间触发该方法查找属性
    #     # 要么返回AttrError，要么返回一个属性
    #     return super().__getattribute__(item)

    def __setattr__(self, key, value):
        # 设置属性时，调用该方法设置属性
        print('---设置属性时调用__setattr__')
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        # 删除属性时调用该方法
        print('---删除属性时调用__delattr__')
        return super().__delattr__(item)



a = Test()
a.name = 10

del a.name

print(a.name)

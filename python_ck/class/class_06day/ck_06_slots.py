# __dict__ 每创建一个实例绑定一个__dict__,每个创建一些实例属性,创建实例多容易消耗内存

# __slots__ 限制对象的属性

class Base(object):

    # 指定类对象所能使用的属性
    # 节约内存,定义了__slots__后,那么该对象不会在生产__dict__属性
    __slots__ = ['name']
    # pass

a = Base()
# 实例仅能使用name属性
a.name = 'tan'
# a.age = 100
# print(a.__dict__)


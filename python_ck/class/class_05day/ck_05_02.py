# 类的3个内置装饰器

class Mytest(object):

    @classmethod  # 装饰后为类方法，cls代表类本身
    def class_method(cls):
        print('classmethod装饰器')

    @staticmethod  # 装饰后为静态方法，实例和类都可调用
    def static_method():
        print('staticmethod装饰器')

    @property  # 设定为只读属性，return的属性不可更改
    def property_(self):
        print('property装饰器')
        return '返回属性'


Mytest.class_method()
Mytest.static_method()
# Mytest.property_

o = Mytest()
o.property_
o.static_method()
o.class_method()

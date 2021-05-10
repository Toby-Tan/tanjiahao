# 描述器类
class Filed(object):
    """
    类里面包含了下面任意一个方法，则该类为描述器类
    """

    def __get__(self, instance, owner):
        print('获取属性的时候被触发')
        return self.value

    def __set__(self, instance, value):
        print('设置属性的时候被触发')
        self.value = value

    def __delete__(self, instance):
        print('删除属性的时候被触发')
        del self.value

class Model(object):
    a = Filed()
    name = 'tan'


m = Model()
m.a = 1000
# print(m.a)

del m.a
print(m.a)

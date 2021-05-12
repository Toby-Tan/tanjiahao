'''
@Author :唐三
@Date   :2021/5/12 23:15
@Desc   :
创建一个对象，会把属性添加到__dict__属性里面。__dict__是个字典
定义了__slots__方法会覆盖__dict__方法
'''
class Base():
    # 指定类属性
    # 节约内存
    __slots__ = ['name']


a = Base()
a.name = 'tanjiahao'
# a.age = 18

class A(object): __slots__ = ('a', 'b', 'c')
class B(A): __slots__ = 'abcd'
print(A.__slots__)
print(repr(B.__slots__))
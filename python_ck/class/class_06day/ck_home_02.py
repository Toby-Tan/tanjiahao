class Myclass(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('-----str-----被调用')
        return self.name

    def __repr__(self):
        print('repr被触发')
        return '<Mytest.object-{}>'.format(self.name)

    def __call__(self, *args, **kwargs):
        self.name = self.name()
        print('___call___被触发')


# m = Myclass('tanjiahao')
# print(m)
# str(m)
# format(m)
# repr(m)

# a= '1000'
#
# def fun():
#     print('____function___')
#
# fun()
# m()

# 通过类实现装饰器  __call__

@Myclass
def test_01():
    print('被类装饰')

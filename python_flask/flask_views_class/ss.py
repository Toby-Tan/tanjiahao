class A(object):
    def set(self, a, b):
        x = a + b
        print(x)
        # return x

    def geta(self, a, b):
        func = getattr(self, 'set', None)
        return func(a, b)


res = A()
res.geta(a=4, b=5)

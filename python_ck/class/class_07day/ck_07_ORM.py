# 描述器类
class CharFiled:
    """
    类里面包含了下面任意一个方法，则该类为描述器类
    """

    #
    def __init__(self, max_length,null):
        self.max_length = max_length
        self.null = null

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                if self.null:
                    self.value = value
                elif self.null is False:
                    if value:
                        self.value = value
                    else:
                        raise ValueError('value is not null')
            else:
                raise ValueError('{} Value length must be {}'.format(value, self.max_length))
        else:
            raise TypeError('{} Type error,need str value'.format(value))

    def __delete__(self, instance):
        self.value = None

    def __get__(self, instance, owner):
        return self.value


class UserModel(object):
    name = CharFiled(max_length=10, null=False)


a = UserModel()
a.name = '1'
print(a.name)

# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# print(isinstance(A(), A))  # returns True
# print(type(A()) == A)  # returns True
# print(isinstance(B(), A) ) # returns True
# print(type(B()) == A)  # returns False
#
# print(type(B()))
# print(A)

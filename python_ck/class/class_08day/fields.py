

class BaseFiled(object):
    pass

class CharFiled(BaseFiled):
    """
    类里面包含了下面任意一个方法，则该类为描述器类
    """
    def __init__(self, max_length=20, null=True):
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

    def __get__(self, instance, owner):
        return self.value


class BoolFiled(BaseFiled):

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise ValueError

    def __get__(self, instance, owner):
        return self.value


class IntFiled(BaseFiled):

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError

    def __get__(self, instance, owner):
        return self.value



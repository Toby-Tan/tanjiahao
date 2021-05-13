'''
@Author :唐三
@Date   :2021/5/12 22:50
@Desc   :私有属性
python伪私有属性
'''
class Myclass():
    __user = 'tan'


# a = Myclass()
print(Myclass.__dict__)
# print(a._Myclass__user)
# 自定义元类
# 自定义元类必须继承type
# type创建类有三个参数（name,bases,attr）
# 第一个参数：name表示类名称，字符串类型
# 第二个参数：bases表示继承对象（父类），元组类型，单元素使用逗号
# 第三个参数：attr表示属性，这里可以填写类属性、类方式、静态方法，采用字典格式，key为属性名，value为属性值
class MyMetaClass(type):

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print('自定义元类')
        for k, v in list(attr_dict.items()):
            attr_dict.pop(k)
            attr_dict[k.upper()] = v
            # break

        return super().__new__(cls, name, bases, attr_dict)


class Test(metaclass=MyMetaClass):
    name = 'tanjiahao'
    age = 18
    gender = '男'

class MyClass(Test):
    pass

# print(type(MyClass))
print(Test.__dict__)
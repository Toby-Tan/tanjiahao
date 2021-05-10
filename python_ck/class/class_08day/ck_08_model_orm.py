# 利用元类实现模型类

from class_08day.fields import BaseFiled, CharFiled, IntFiled, BoolFiled


class FieldMetaClass(type):
    def __new__(cls, name, bases, dic, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, dic)
        else:
            table_name = name.lower()  # 表名转小写
            fields = {}
            for k, v in dic.items():
                if isinstance(v, BaseFiled):
                    fields[k] = v
            # print(dic)
            dic['t_name'] = table_name
            dic['t_fileds'] = fields


            return super().__new__(cls, name, bases, dic)


class BaseModel(metaclass=FieldMetaClass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            # print(k, v)

    def save(self):
        t_name = self.t_name
        fileds = self.t_fileds
        filed_dict = {}
        print(self)
        for filed in fileds.keys():
            filed_dict[filed] = getattr(self, filed)
            # print(getattr(self, filed))
        sql = "INSERT INTO {} VALUE {}".format(t_name, tuple(filed_dict.values()))
        print(sql)


class User(BaseModel):
    username = CharFiled()
    pwd = CharFiled()
    age = IntFiled()
    live = BoolFiled()


xiao = User(username='tanjiahao', pwd='111', age=18, live=True)
xiao.save()

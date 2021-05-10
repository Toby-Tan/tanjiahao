# 面向对象三大特征
# 封装、继承、多态
# python伪多态

class Base(object):
    def run(self):
        print('=====父类=====动物类')

class Cat(Base):
    def run(self):
        print('=====子类=====卖萌')

class Dog(Base):
    pass

base_obj = Base()
cat_obj = Cat()
dog_obj = Dog()

def func(obj):
    obj.run()

func(base_obj)
func(cat_obj)
func(dog_obj)
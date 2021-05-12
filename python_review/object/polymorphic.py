'''
@Author :唐三
@Date   :2021/5/12 22:21
@Desc   :面向对象3大特征
1.封装
2.继承
3.多态--python伪多态
子类继承并重写父类方法，调用子类对象的方法就称为多态
'''

class Base(object):

    def run(self):
        print('===BaseRun===')

class Dog(Base):

    def run(self):
        print('===DogRun===')

class Cat(Base):
    def run(self):
        print('===CatRun===')

class MyRun(object):
    def run(self):
        print('===MyRun===')


cat_obj = Cat()
dog_obj = Dog()
my_obj = MyRun()

def all_run(base_obj):
    base_obj.run()

all_run(cat_obj)
all_run(dog_obj)
all_run(my_obj)
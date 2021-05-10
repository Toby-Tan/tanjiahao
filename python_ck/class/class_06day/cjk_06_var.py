# var   公共属性,都可以访问
# _var  表面私有，实际上外部仍然可以访问
# __var 真正的私有属性,外部不可访问

class Test:

    public_attr = 100
    _private_attr = 200
    __private_attr1 = 300

class Test_sub(Test):
    pass

# 子类访问父类属性,私有属性也是可以继承的

sub = Test_sub()
# 访问公共属性
print(sub.public_attr)
# 访问_属性
print(sub._private_attr)
# 访问私有__属性,报错
print(sub.__private_attr1)

print(sub.__dict__)
a = Test()

# print(a.public_attr)
# print(Test.public_attr)
#
# print(a._private_attr)
# print(Test._private_attr)


# 私有属性对外不能直接访问，双下划线开头的属性改了名字，加了：_类名 才可以访问
# print(a._Test__private_attr1)
# print(Test.__private_attr1)
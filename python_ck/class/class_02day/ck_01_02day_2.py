# 列表推导式
urls = ['url{}'.format(i) for i in range(1, 101)]
# print(urls)

# 字典推导式
li = {i: i + 1 for i in range(11)}
# print(li)
test = {'BIDUPSID': '{}'.format(i) for i in range(10)}

lis = 'id=2;name=tan;ege=18'
# dicts = {item.split('=')[0]: item.split('=')[1] for item in lis.split(';')}
dicts = {}
for i in lis.split(';'):
    key = i.split('=')[0]
    var = i.split('=')[1]
    dicts[key] = var

print(dicts)


# 通过yield自定生成器
def fun_gen():
    yield 100
    print('test')
    yield 1000


#
# res = fun_gen()
# print(res)
#
# print(next(res))
# print(next(res))


# 可迭代对象：可for遍历的都是可迭代对象
li1 = [1, 2, 3, 4]

li2 = iter(li1)  # iter()


# print(next(li2))

# 闭包满足条件
# 1.函数中嵌套函数
# 2.外层函数返回内层嵌套函数名
# 3.内层嵌套函数有引用外层的一个非全局变量
# 作用：实现数据的锁定，提高稳定性

def func():
    num = 0

    def num_count():
        print(num)
    return num_count


res = func()
res()
# 偏函数

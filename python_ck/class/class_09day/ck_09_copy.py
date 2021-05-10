# 深浅拷贝

# 浅拷贝会吧引用拷过去，引用数据发生改变，拷贝的数据也发生变化

# 深拷贝会把内层引用的数据都复制一份重新存起来。引用的数据发生变化，不会影响深拷贝的数据


# 垃圾回收机制

# 引用计数
# 当数据被引用时，引用n次则计数n次，当数据没有被引用后，计数为0触发垃圾回收机制
a = 'abc'
a1 = 'abc'
b = 'xxx'
# a = b
# 循环引用会存在内存泄露
li1 = [1, 2]
li2 = [11, 22]
li1.append(li2[1])
li2.append(li1[1])

# 标记-清除
# 有没有被全局变量引用，没有就清除

# 分代收集

w = [1, 2, 3, ]
w = a
w1 = [11, w]


# print(w1)


# 10 9 8 7 6 5 4 3 2 1
#  1 2 3 4 5 6 7 8 9 10

def accout(ci):
    sum_sd = 0
    sum_fwc = 0
    for i in range(1, ci + 1):
        sum_fwc += i
    for e in range(1, ci + 1):
        sum_sd += e
    print(sum_fwc + sum_sd)


accout(5)

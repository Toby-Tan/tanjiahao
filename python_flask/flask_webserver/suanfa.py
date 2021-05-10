# 冒泡排序
def maopao(fun):
    def t_01(args, **kwargs):
        lens = len(args)
        for i in range(lens - 1):
            for j in range(lens - 1 - i):
                if args[j] > args[j + 1]:
                    args[j], args[j + 1] = args[j + 1], args[j]
        return fun(args, **kwargs)

    return t_01


#
#
@maopao
def result(*args, **kwargs):
    print(args)


#
li = [5, 4, 1, 7, 8, 2, 22, 0, 3, 6, 344343, 1221, 0]
result(li)
#
# def foo(num):
#     while num < 10:
#         print("starting...")
#
#         num = num + 1
#         yield num
#
#
# for n in foo(2):
#     # print(foo(2))
#     print(n)

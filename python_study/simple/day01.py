'''
@Author :唐三
@Date   :2021/5/12 23:51
@Desc   :
'''

my_name = 'tanjiahao'
my_height = 74  # inches
my_weight = 180  # lbs

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
"""
1.修改所有的变量名字，把它们前面的``my_``去掉。确认将每一个地方的都改掉，不
只是你使用``=``赋值过的地方。
2. 试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什
么都打印出来”。
3. 在网上搜索所有的 Python 格式化字符。
4. 试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的
计算功能来完成。
"""
# 1.重新定义所有变量
def fun():
    return 'aaa'
    # print('aaa')
# 2.使用format函数格式化字符
myname = f'我的名字:{fun}'
print(myname)

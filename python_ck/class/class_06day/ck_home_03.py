# 重写上下文管理器

class Myopen(object):

    def __init__(self, filename, open_mode, encoding='utf-8'):
        self.filename = filename
        self.open_mode = open_mode
        self.encoding = encoding

    def __enter__(self):
        # 返回文件句柄
        self.f = open(self.filename, self.open_mode, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type) # 报错类型
        # print(exc_val)  # 报错内容value
        # print(exc_tb)   # 报错追踪Traceback object
        # 关闭文件流
        self.f.close()


with Myopen('test.txt', 'w') as f:
    f.write('又是快乐学习的一天')

with Myopen('test.txt', 'r') as f:
    content = f.read()
    # print(s)
    print(content)

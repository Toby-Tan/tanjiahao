

class Myopen():
    def __init__(self,filename,pattern):
        self.filename = filename
        self.pattern = pattern

    def __enter__(self):
        self.f = open(self.filename,self.pattern,encoding='utf-8')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


# with Myopen('mytest1.txt','a+')as f:
#     f.write('Myopen creat text\n')

with Myopen('mytest.txt','a+')as f:
    # 指针偏移
    f.seek(0, 0)
    # 获取文件游标
    print(f.tell())
    res = f.read()
    print(f.tell())
    print(res)
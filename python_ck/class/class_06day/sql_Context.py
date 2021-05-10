# 实现一个上下文管理器，用来链接数据库，关闭数据库
import pymysql


# import pandas as pd


class MyConnectDb(object):
    # 指定类对象所能使用的属性,不可添加__slots__外的其他属性,可以节约内存
    # __slots__ = ['host', 'user', 'password', 'db', 'charset', 'conn', ]

    def __init__(self, data_conf):
        self.conn = pymysql.connect(**data_conf)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        # 返回文件游标
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type) # 报错类型
        # print(exc_val)  # 报错内容value
        # print(exc_tb)   # 报错追踪Traceback object
        # 关闭文件流
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


DTATBAST_CONF = dict(
    host='localhost',
    user='root',
    password='123456',
    db='django_restful',
    charset='utf8',
)

with MyConnectDb(DTATBAST_CONF) as cursor:
    # 查询sql
    for i in range(50):
        data = {
            # 'id': i,
            'name': 'tanjiahao',
            'email': '506000311@qq.com',
            'groups': 'http://127.0.0.1:8000/groups/1/',
        }

        s_sql = "INSERT INTO api_user(username,email,groups) VALUES('{}', '{}', '{}');".format(data['name'],
                                                                                                data['email'],
                                                                                                data['groups'])
        # print(s_sql)
        cursor.execute(s_sql)
        i += 1

    # 使用 execute()  方法执行 SQL 查询

    # cursor.execute(s_sql)  # 返回的是数据的行数
    # data = cursor.fetchall()  # fetchall()方法返回多个元组数据,也就是多行记录
    # print(data)

    # cursor.execute('SELECT username FROM api_user;')
    # data1 = cursor.fetchone()  # fetchone()方法返回单个元组数据,也就是一行记录
    # print(data1)

    # for j in data:
    #     print(j[1])

import pymysql


class ConnectMysql():

    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.passwrod = password
        self.database = database
        # self.charset = charset

    def __enter__(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.passwrod,
            database=self.database,
            # charset=self.charset
        )
        # 创建游标对象
        self.cursor = self.conn.cursor()
        # self.cursor.execute(self.sql)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标对象
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


sql = 'SELECT * FROM api_user;'
with ConnectMysql('localhost', 3306, 'root', 'passwrod', 'django_restful')as cursor:
    cursor.execute(sql)
    # 获取所有记录列表
    res = cursor.fetchall()
    for row in res:
        print(row)
"""
实现一个简单的登录接口
"""
from flask import Flask, request, render_template
import pymysql


app = Flask(__name__)

class ConMysql(object):

    def __init__(self,host,port,user,pwd,database,sql=None):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.database = database
        self.sql = sql

    def __enter__(self):
        self.con = pymysql.connect(host=self.host,
                              port=self.port,
                              user=self.user,
                              password=self.pwd,
                              database=self.database,
                              )
        self.cursor = self.con.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()

def get_user_data():
    sql = 'SELECT * FROM test_user;'
    with ConMysql(host='localhost',port=3306,user='root',pwd='123456',database='django_restful') as cursor:
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

def login_check():
    data = get_user_data()
    username = data[0]
    password = data[1]
    user = request.form.get('user')
    pwd  = request.form.get('passwrod')
    if user == username and pwd == password:
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    if login_check():
        return 'success login'
    return '账号或密码错误'


@app.route('/user')
def user():
    res = request.args.get('id')
    if res == '1':
        return '1'
    return 'error123456'

if __name__ == '__main__':
    app.run(debug=True)

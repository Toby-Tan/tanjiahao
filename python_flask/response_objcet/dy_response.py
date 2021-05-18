"""
实现一个简单的登录接口
"""
import json

from flask import Flask, request, render_template, jsonify
import pymysql

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


class ConMysql(object):

    def __init__(self, host=None, port=None, user=None, pwd=None, database=None):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.pwd = '123456'
        self.database = 'django_restful'

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
    sql = 'SELECT phone FROM test_user;'
    with ConMysql() as cousor:
        cousor.execute(sql)
        res = cousor.fetchall()
        return res


def login_check():
    data = get_user_data()
    print(data)
    phone_li = []
    for i in data:
        for phone in i:
            phone_li.append(phone)
    print(phone_li)
    username = data[0]
    password = data[1]
    user = request.form.get('user')
    pwd = request.form.get('passwrod')
    if user == username and pwd == password:
        return True
    return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    success_re = {"code": "0", "msg": "success login"}
    erro_re = {"code": "101", "msg": "账号或密码错误"}
    msg = dict(code=101, msg='账号或密码错误')
    n = json.dumps(success_re)
    # print(type(n))
    # print(n)
    load = json.loads(n)
    # print(type(load))
    # print(load)
    if login_check():
        return jsonify(success_re)
    return jsonify(msg)


# @app.route('/user')
# def user():
#     res = request.args.get('id')
#     if res == '1':
#         return
#     return 'error123456'

if __name__ == '__main__':
    app.run(debug=True)

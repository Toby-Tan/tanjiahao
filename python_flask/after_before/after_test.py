from flask import Flask, g, render_template
import pymysql

app = Flask(__name__)

# app_ctx = app.app_context()
# app_ctx.push()


def connect_to_database():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='django_restful',
        charset='utf8mb4'
    )
    return conn.cursor()


# 在服务的第一个请求执行
# 用来初始化服务器的一些设置
# @app.before_first_request
# def bf_first_req():


# 在请求之前执行
# 用来统计流量，阅读数，签名等
@app.before_request
def get_db():
    if 'db' not in g:
        g.db = connect_to_database()

# 在请求结束之后执行，viewfunction报错则失效
# 用来构造响应对象
# @app.after_request
# def make_response(response):
#     response.headers['server'] = 'i do'
#     return response

# 在请求结束之后执行，不论有没有报错
# 可以用来关闭数据库连接
@app.teardown_request
def teardown_db(exception):
    print(g.db)
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    sql = 'SELECT phone FROM test_user;'
    g.db.execute(sql)
    res = g.db.fetchall()
    print(res)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect, request, url_for

app = Flask(__name__)



@app.route('/')
def index():
    if request.args.get('username') is None:
        # 重定向端点名称，重定向时可以加关键字参数
        return redirect(url_for('error_point',username="tanjiahao"))
    return 'index'

@app.route('/login',endpoint='login_point')
def login():
    return 'login'

@app.route('/error',endpoint='error_point')
def error():
    return 'error'


if __name__ == '__main__':
    app.run(debug=True)
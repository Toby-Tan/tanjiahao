from flask import Flask, redirect, request, url_for

app = Flask(__name__)



@app.route('/')
def index():
    if request.args.get('username') is None:
        # 重定向端点名称，重定向时可以加关键字参数
        return redirect(url_for('login',username="tanjiahao"))
    return 'index'

@app.route('/login',endpoint='login')
def login():
    return 'login'



if __name__ == '__main__':
    app.run(debug=True)
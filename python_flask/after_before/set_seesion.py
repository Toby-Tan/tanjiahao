from datetime import timedelta

from flask import Flask, request, session, abort

app = Flask(__name__)
# with app.app_context():
#     init_db()

app.config['SECRET_KEY'] = 'aaa'
app.config['SESSION_COOKIE_NAME'] = 'session_id'
#在config.py中配置session参数PERMANENT_SESSION_LIFETIME,这个值的数据类型是datetime.timedelay类型
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
# session.permanent = True #默认为31天


@app.route('/index')
def index():
    if not session.get('user'):
        abort(401)
    # return 'index'
    return '回到首页'

@app.route('/login')
def login():
    username = request.args.get('username')
    pwd = request.args.get('pwd')
    if username and pwd:
        session['user'] = username
        return '登录成功'
    return '没有登录'

@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        return '登出成功'
    return '未登录'



if __name__ == '__main__':
    app.run(debug=True)
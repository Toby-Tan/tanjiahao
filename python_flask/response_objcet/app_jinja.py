import json
import time
from datetime import datetime

from flask import Flask, render_template, flash, session, message_flashed, current_app, redirect, url_for
from werkzeug.local import LocalStack

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ssss'

# flash方法
def my_flash(key, message):
    session[key] = message
    return session[key]

# 注册过滤器，装饰器注册
# @app.template_filter('s_time')
def str_time(timestamp):
    return datetime.fromtimestamp(timestamp)

# 注册过滤器，集中注册
app.add_template_filter(str_time,'s_time')

# 注册测试，装饰器注册
# @app.template_test('isjson')
def check_josn(str):
    try:
        json.loads(str)
        return True
    except ValueError:
        return False

# 注册测试，集中注册
app.add_template_test(check_josn,'isjson')

# 注册全局函数。装饰器注册
# @app.template_global('g_function')
def get_global():
    return "global function"

# 注册全局函数，集中注册
app.add_template_global(get_global,'g_function')


"""
作为一个全局变量去引用
1. context_processor 作为一个装饰器修饰一个函数
2. 函数的返回结果必须是 dict, 然后其 key 将会作为变量在所有模板中可见
当你的很多视图函数中需要回传一个相同的变量的时候，这个时候就可以考虑使用 context_processor 了
"""
@app.context_processor
def context_time():
    def str_time(timestamp):
        return datetime.fromtimestamp(timestamp)
    return {"c_time":str_time}


@app.route('/',endpoint='index')
def index():
    # my_flash('success','login success')
    projects = [
        {"project_name": "项目1", "interface_num": "10", "creat_time": int(time.time())},
        {"project_name": "项目2", "interface_num": "11", "creat_time": int(time.time())},
        {"project_name": "项目3", "interface_num": "12", "creat_time": int(time.time())}
    ]
    return render_template('home.html',
                           title='jinja渲染模板',
                           projects=projects,
                           pm=None,
                           test_json='{"name":"tanjiahao"}'
                           )

@app.route('/login/<username>')
def login(username):
    my_flash('user',username)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

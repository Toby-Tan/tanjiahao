# ids = [1,2,3]
# b = 0
# print(f'{ids}{b}')
# print('{}{}'.format(ids,b))
from flask import Flask, request, redirect

app = Flask(__name__)


# 动态路由
# 两种形式
# 第一种形式   # flask 的request.args().get()方法获取url参数
# @app.route('/cases/')
# def get_case():
#     uid = request.args.get('uid')
#     return f'{uid}'


# 第二种形式
# <int:id> ; <float:id>; <string:id>; <path:id>可以加斜杠;<uuid:id>
# @app.route('/cases/<id>')
# def get_case(id):
#     return f'{id}'


# 另外一种注册路由机制,集中注册机制;  适合大型项目
# 装饰器注册;  适合中小型项目



@app.route('/')
def home():
    return 'home'

# @app.route()里面的参数[redirect_to='/']重定向不会执行该视图函数
# return redirect('/'),通过return  redirect方法会执行视图函数
# 默认参数,1.defaults = {'id':3}
# 2.视图函数里定义id = 3
@app.route('/cases', methods=['GET'], endpoint='getcase', )
def get_case():
    print('重定向被执行')
    return redirect('/')


# app.add_url_rule('/cases', view_func=get_case, methods=['GET'], endpoint='case')
# # 路由:url和视图函数的绑定关系;; 一个路由对应一个端点:端点默认为视图函数的名称
# print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)

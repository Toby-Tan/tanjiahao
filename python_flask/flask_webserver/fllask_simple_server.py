import requests
from flask import Flask, render_template

# 定义Application
app = Flask(
    __name__,
    # template_folder='templates'
)


# 定义路由，视图函数 view function
@app.route('/')
def index():
    f = render_template('index_1.html')
    return f


# 开启web服务器
# flask自带的，仅用与调试，测试，开发===》不用于生产环境 uwsgi,nginx
if __name__ == '__main__':

    app.run()

from flask import Flask, render_template
import time

# 定义Application
app = Flask(

    __name__,
    # html模板文件存放位置
    # template_folder='templates',
    # 告诉程序静态文件放在哪个位置
    static_folder='static',
    # 告诉程序处理静态文件的url
    static_url_path='/static',
)


# 定义一个装饰器统计函数运行时间
def log_time(func):
    def swapper(*args, **kw):
        s_time = time.time()
        res = func(*args, **kw)
        print('耗时：{}'.format(time.time() - s_time))
        return res

    return swapper


# 定义一个装饰器,实现统计流量
def log_flow(func):
    num_l = [0]

    def swapper(*args, **kw):
        res = func(*args, **kw)
        if res:
            num_l[0] += 1
        print('访问了{}次'.format(num_l[0]))
        return res

    return swapper


# 定义路由，视图函数 view function
# @app.route('/hello') # 多url的路由
# @app.route('/')
# @log_time
# @log_flow
# def index():
#     """
#     MVC：分层设计思想
#     model view control
#     view -》视图，发送请求-》control 接收请求跳转到对应的模型model -》
#     -》model 处理数据，实现各个模块的功能-》通过control返回操作结果给view
#     """
#     # 1.接受参数
#     # 2.调用对应的函数处理数据（model层)
#     # 3.构建响应结果
#     f = render_template('index.html')
#     return f


# 开启web服务器
# flask自带的，仅用与调试，测试，开发===》不用于生产环境 uwsgi,nginx
# if __name__ == '__main__':
#     app.run(debug=True)
    # 调试打开debug=True
    # 1.可以通过页面访问错误信息，
    # 2.可以自动重启

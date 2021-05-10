# 搭建服务
# 监听动作,while ,0.1轮询
# 处理程序
# 返回数据到套接字,生成一个响应对象

# wsgi协议；
# 在Webserver和application之间通信
# flask是一个符合wsgi的 application 的web框架
"""
为什么需要Nginx
一个普通的个人网站，访问量不大的话，当然可以由uWSGI和Django构成。
但是一旦访问量过大，客户端请求连接就要进行长时间的等待。
这个时候就出来了分布式服务器，我们可以多来几台web服务器，都能处理请求。
但是谁来分配客户端的请求连接和web服务器呢？Nginx就是这样一个管家的存在，由它来分配。
这也就是由Nginx实现反向代理，即代理服务器。
"""
from wsgiref.simple_server import make_server


def index(params):
    return params


def login(params):
    return params


def projects(params):
    return params


def interface(params):
    return params


patterns = {
    '/': index,
    '/login': login,
    '/projects': projects,
    '/interface': interface,
}


def app(env, start_response):
    # 获取Path信息,浏览器输入的路径
    url = env.get('PATH_INFO')
    params = env.get('QUERY_STRING')
    print(url)
    if url not in patterns.keys():
        # 构造响应体
        start_response('404 not found', [('content-type', 'text/plain')])
        return [b'404 not ']
    else:
        start_response('200 ok', [('content-type', 'text/plain')])
        res = patterns.get(url)
        # if res is None:
        #     start_response('404 not found', [('content-type', 'text/plain')])
        #     return [b'page not found']
        return [res(params).encode()]


server = make_server('', 6001, app)
server.serve_forever()

#
# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     yield "Hello world!\n"


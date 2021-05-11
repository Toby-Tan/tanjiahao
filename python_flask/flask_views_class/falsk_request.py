from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    a = request
    # 请求相关，数据存放在环境变量内，可以通过request的一些方法获取
    # 获取url参数数据
    get_data = request.args
    # 获取表单数据
    get_form = request.form
    # 获取json数据
    get_json = request.json
    # 获取文件数据
    get_file = request.files
    # 获取values,(form+args)
    get_values = request.values
    # 获取环境变量
    get_environ = request.environ
    # 获取content_type
    get_content_type = request.content_type
    # 判断是不是Josn类型数据，通过content_type
    is_json = request.is_json


    return 'index'


from flask import Flask, redirect, request, url_for, render_template,abort

app = Flask(__name__)

# 全局错误处理
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    print('404被调用')
    return render_template('error_404.html'),404

# 全局错误处理
@app.errorhandler(500)
def page_not_found(error):
    return render_template('error_500.html'),500


class UserError(Exception):
    pass


@app.errorhandler(UserError)
def page_not_found(error):
    return render_template('error_404.html'),404


@app.route('/')
def index():
    if request.args.get('username') is None:
        # 1.直接retrun一个错误页面
        # return render_template('error_404.html'),404
        # 第二种flask内置函数abort()
        abort(404)
        # 第三种自定义错误raise
        # raise UserError()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# import re
#
# from flask import Flask, request, abort, render_template, Response, redirect, jsonify
#
# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
#
# @app.route('/')
# def redirect_register():
#     return redirect('/register')
#
#
# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     phone = request.form.get('phone')
#     pwd = request.form.get('pwd')
#     confirm_pwd = request.form.get('confirm_pwd')
#     # 构建一个Response对象，传入abort
#     if request.method == 'GET':
#         return render_template('index.html')
#     res_phone_empty = jsonify({"code":"1001","msg":"手机号不能为空"})
#     res_phone_error =  jsonify({"code":"1002","msg":"手机号格式错误"})
#     res_pwd_empty = Response(render_template('index.html', msg='密码不能为空'), 412,
#                              content_type="text/html;charset=utf-8")
#     res_pwd_error = Response(render_template('index.html', msg='密码至少6位字符'), 412,
#                              content_type="text/html;charset=utf-8")
#     confirm_pwd_error = Response(render_template('index.html', msg='密码不一致，请重新输入'), 412,
#                                  content_type="text/html;charset=utf-8")
#     if not phone:
#         return res_phone_empty
#     pattern = re.compile('^1[356789]\d{9}$')
#     print(re.match(pattern, phone))
#     if not re.match(pattern, phone):
#         return res_phone_error
#     if not pwd:
#         abort(res_pwd_empty)
#     if len(pwd) < 6:
#         abort(res_pwd_error)
#     if pwd != confirm_pwd:
#         abort(confirm_pwd_error)
#     return "注册成功"
#
# if __name__ == '__main__':
#     app.run(debug=True)

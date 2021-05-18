import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Regexp, DataRequired, length, EqualTo, ValidationError
from python_flask.response_objcet.dy_response import ConMysql


class Mobile:
    regex = re.compile(r'^1[35789]\d{9}$')

    def __init__(self, message=None):
        if message is None:
            self.message = '手机号格式错误'
        else:
            self.message = message

    def __call__(self, form, field):
        match = self.regex.match(field.data)
        print(match)
        if not match:
            message = self.message
            raise ValidationError(message)
        return match


class ExistPhone:

    def __init__(self, message=None):
        if message is None:
            self.message = '手机号已存在'
        else:
            self.message = message

    def serch_phone(self):

        sql = 'SELECT phone FROM test_user;'
        with ConMysql() as cousor:
            cousor.execute(sql)
            res = cousor.fetchall()
            return res

    def check_exist(self,data):
        phone_li = []
        res = self.serch_phone()
        for i in res:
            for phone in i:
                phone_li.append(phone)
        if data in phone_li:
            return True
        else:
            return False

    def __call__(self, form, field):
        exist = self.check_exist(field.data)
        if exist:
            message = self.message
            raise ValidationError(message)
        return field.data


class RegisterForm(FlaskForm):
    phone = StringField(label="手机号码", render_kw={"style": "background: #00cccc"},
                        validators=[Mobile(message='手机号格式错误，请重新输入'), ExistPhone(message='手机号已被注册，请确认'),DataRequired(message='手机号不能为空')])
    pwd = PasswordField(label="密码",
                        validators=[length(6, 12, message='密码长度限制6~12位，请重新输入'), DataRequired(message="密码不能为空")])
    confirm_pwd = PasswordField(label="确认密码", validators=[EqualTo('pwd', message='密码输入不一致，请重新输入')])

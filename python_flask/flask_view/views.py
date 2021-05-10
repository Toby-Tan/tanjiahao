from flask import redirect


def get_case():
    return 'cases_list'


def index():
    return '首页'


def redir_home():
    print('重定向到/cases页面')
    return redirect('/cases')
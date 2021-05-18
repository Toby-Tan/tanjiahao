from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库配置，可配置多个数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/demo"
# app.config['SQLALCHEMY_BINDS'] =
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 建立多个数据库连接SQLALCHEMY_BINDS
# app.config['SQLALCHEMY_BINDS'] = {
#
# }
db = SQLAlchemy(app)
migrate = Migrate(app,db)
# db.create_all()
"""
Migrate初始化数据库环境
1.set FLASK_APP=simple_orm.py(model文件名)
2.flask db init
创建表
>>> from simple_orm import db
>>> db.create_all()
flask db migrate
更新数据库表
flask db upgrade
回退
flask db downgrade
"""

"""
交互环境下创建数据库表
1.set FLASK_APP=simple_orm.py(model文件名)
2.flask shell
3.from simple_orm(model文件名，不要.py) import db
4.db.create_all()
"""

class User(db.Model):
    # 模型绑定
    __bind_key__ = 'main'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(80),unique=True)

# 运行
with app.app_context() as ctx:
    ctx.push()
    new_user = User(username='tanjiahao', email='demo@qq.com')
    db.session.add(new_user)
    db.session.commit()


@app.route('/')
def index():
    # 插入数据
    new_user = User(username='tanjiahao',email='demo@qq.com')
    db.session.add(new_user)
    db.session.commit()
    return 'index'


@app.route('/query')
def query():
    # 查询数据
    users = User.query.all()
    print(users) # [<User 1>]
    return 'index'

if __name__ == '__main__':

    app.run(debug=True)
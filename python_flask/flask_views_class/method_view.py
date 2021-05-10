from flask import Flask, request
from flask.views import MethodView

app = Flask(__name__)


class ProjeckView(MethodView):
    # methodes = ['POST','GET']

    # decorators=()
    def get(self, pro_id=None):
        if pro_id is None:
            return '获取全部项目'
        return f'获取{pro_id}项目'

    def post(self):
        return '创建一个项目'

    def delete(self, pro_id):
        return f'删除{pro_id}项目'

    def put(self, pro_id):
        return f'更新{pro_id}项目'


f = ProjeckView.as_view('pro')
app.add_url_rule('/project/<pro_id>', methods=['GET', 'DELETE', 'PUT'], view_func=f)
app.add_url_rule('/project/', methods=['GET', 'POST'], view_func=f)

if __name__ == '__main__':
    app.run(debug=True)

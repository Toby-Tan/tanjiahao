from flask import Flask, request
from flask.views import View

app = Flask(__name__)


class Projcets(View):
    def get(self):
        return 'get'

    def post(self):
        return 'post'

    def dispatch_request(self):
        dispatch_pattern = {'GET': self.get, 'POST': self.post}
        method = request.method
        return dispatch_pattern.get(method)()


app.add_url_rule('/project', methods=['GET', 'POST'], view_func=Projcets.as_view('pro'))

if __name__ == '__main__':
    app.run(debug=True)

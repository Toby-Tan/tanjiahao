from valiadtors import RegisterForm
from flask import Flask, request, abort, render_template, Response, redirect, jsonify
import os
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = os.urandom(24)
# print(os.urandom(24))

@app.route('/')
def redirect_register():
    return redirect('/register')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(formdata=request.form)
    if request.method == 'GET':
        return render_template('index.html',form=form)
    # a = form.validate()
    # b = form.data
    if form.validate():
        return 'registered successfully'
    return f'errors{form.errors}'



if __name__ == '__main__':
    app.run(debug=True)

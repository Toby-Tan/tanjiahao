import time

from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload/', methods=['POST'])
def upload_file():
    filetype = ['jpg', 'png', 'xls', 'xlsx', 'xmind']
    file = request.files.get('up')
    file_name = file.filename
    file_type = file_name.split('.')[-1]
    file_path = os.getcwd() + f'\\static\\{file_name}'
    if not file:
        return render_template('index.html')
    if file_type in filetype:
        file.save(file_path)
        return file_path
    else:
        return render_template('index.html')+'格式不支持'
    # file.save(os.path.join(
    #     app.root_path,
    #     app.static_folder,
    #     file_name
    # ))


if __name__ == '__main__':
    app.run(debug=True, port=5002)

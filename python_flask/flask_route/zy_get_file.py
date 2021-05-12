import time

from flask import Flask, render_template, request, send_from_directory
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)
# 限制文件大小为1M
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload/', methods=['POST'])
def upload_file():
    filetype = ['jpg', 'png', 'xls', 'xlsx', 'xmind']
    file = request.files.get('up')
    # >> > secure_filename("My cool movie.mov")
    # 'My_cool_movie.mov'
    file_name = secure_filename(file.filename)
    file_type = file_name.split('.')[-1]
    file_path = os.getcwd() + f'\\static\\{file_name}'
    if not file:
        return render_template('index.html')
    if file_type in filetype:
        file.save(file_path)
        return 'save success'
    else:
        return '文件格式不支持'


@app.route('/upload/<filename>')
def get_upload(filename):
    path = os.getcwd() + '\\static\\'
    return send_from_directory(path, filename)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

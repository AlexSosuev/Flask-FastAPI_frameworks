from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Введите путь к файлу в адресной стоке'

@app.route('/<path:file>/')
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {file}'
    return f'Ваш файл находится в: {escape(file)}'

if __name__ == '__main__':
    app.run(debug=True)
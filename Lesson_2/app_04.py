from flask import Flask,  request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровнь {level}<br>'
    else:
        text = f'Привет, новичок.<br>'
    return f'{text} {request.args}'

if __name__ == '__main__':
    app.run(debug=True)
# Задание 3. Создать страницу, на которой будет форма для ввода логина и пароля, при нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.

from flask import Flask, render_template, request

app = Flask(__name__)

LOGIN = 'admin'
PASSWORD = '1234'

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    login = request.form.get("login")
    password = request.form.get("passwd")

    if login == LOGIN and password == PASSWORD:
        return render_template('succesful.html')
    return render_template('error.html')
   

if __name__ == '__main__':
    app.run()
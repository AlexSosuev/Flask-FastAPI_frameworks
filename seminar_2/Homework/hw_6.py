# Задание №9. Создать страницу, на которой будет форма для ввода имени и электронной почты.
# При отправке которой будет создан cookie файл с данными пользователя.
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти". При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('hw_6_1.html')

@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if name:
        return render_template('hw_6_2.html', name=name)
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('home')))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response

if __name__ == '__main__':
    app.run()
# Задание №6 Создать страницу, на которой будет форма для ввода имени и возраста пользователя 
# и кнопка "Отправить". При нажатии на кнопку будет произведена проверка возраста и переход на 
# страницу с результатом или на страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= 18:
            return redirect(url_for('result', name=name))
        else:
            return redirect(url_for('error'))
    return render_template('hw_3_1.html')

@app.route('/result/<string:name>')
def result(name):
    return render_template('hw_3_2.html', name=name)

@app.route('/error')
def error():
    return render_template('hw_3_3.html')

if __name__ == '__main__':
    app.run()
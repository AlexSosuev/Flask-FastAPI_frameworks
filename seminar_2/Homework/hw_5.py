# Задание №8 Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить". 
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!')
        return redirect(url_for('result'))
    return render_template('hw_5_1.html')

@app.route('/result')
def result():
    return render_template('hw_5_2.html')

if __name__ == '__main__':
    app.run()
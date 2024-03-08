# Задание №7 Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        square = number * number
        return redirect(url_for('result', number=number, square=square))
    return render_template('hw_4_1.html')

@app.route('/result/<int:number>/<int:square>')
def result(number, square):
    return render_template('hw_4_2.html', number=number, square=square)

if __name__ == '__main__':
    app.run()
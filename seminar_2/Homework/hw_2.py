# Задание №5. Создать страницу, на которой будет форма для ввода двух чисел и выбор операции 
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить" При нажатии на кнопку будет 
# произведено вычисление результата выбранной операции и переход на страницу с результатом.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')
        result = calculate_result(num1, num2, operation)
        return redirect(url_for('result', result=result))
    return render_template('hw_2_1.html')

@app.route('/result/<float:result>')
def result(result):
    return render_template('hw_2_2.html', result=result)

def calculate_result(num1, num2, operation):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'division':
        return num1 / num2
    
if __name__ == '__main__':
    app.run()
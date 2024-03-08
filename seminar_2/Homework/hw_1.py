# Задание №4 Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить". 
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        word_count = len(text.split())
        return redirect(url_for('result', count=word_count))
    return render_template('hw_1_1.html')

@app.route('/result/<int:count>')
def result(count):
    return render_template('hw_1_2.html', count=count)

if __name__ == '__main__':
    app.run()
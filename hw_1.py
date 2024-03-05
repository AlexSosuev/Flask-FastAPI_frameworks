from flask import Flask,  render_template

app = Flask(__name__)

# Задание №8 Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для каждой отдельной страницы. Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.

@app.route('/about_us/')
def about_us():
    context = {'title': 'О нас'}
    return render_template('about_us.html', **context)

@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)

# Задание №9 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

@app.route('/cloth/')
def cloth():
    context = {'h1': 'Одежда'}
    return render_template('cloth.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'h1': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/jacket/')
def jacket():
    context = {'h1': 'Куртка'}
    return render_template('jacket.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
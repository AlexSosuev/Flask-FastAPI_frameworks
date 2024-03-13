# Задание №8. Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, redirect, url_for
from models_hw7 import db, User
from forms_hw7 import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw_7.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('hw7.html', form=form)

@app.route('/success')
def success():
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
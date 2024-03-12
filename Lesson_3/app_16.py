from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

"""
Герерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        #Обработка данных из формы
        pass
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
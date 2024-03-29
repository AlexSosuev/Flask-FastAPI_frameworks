from flask import Flask
from flask_wtf.csrf import CSRFProtect

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

@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'

if __name__ == '__main__':
    app.run(debug=True)
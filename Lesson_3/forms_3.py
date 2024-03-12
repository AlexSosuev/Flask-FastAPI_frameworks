from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Pasword', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Pasword', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Pasword', validators=[DataRequired(), EqualTo('password')])
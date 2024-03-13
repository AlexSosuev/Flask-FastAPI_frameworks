# Задание 1. Создать базу данных для хранения информации о студентах университета. База данных должна содержать две таблицы: "Студенты" и "Факультеты". 
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета. В таблице "Факультеты" должны быть следующие 
# поля: id и название факультета. Необходимо создать связь между таблицами "Студенты" и "Факультеты". Написать функцию-обработчик, которая будет выводить 
# список всех студентов с указанием их факультета.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 'муж'
    female = 'жен'


class Fags(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    fag_name = db.Column(db.String(80), nullable=False)
    student = db.relationship('Students', backref=db.backref('fags'), lazy=True)

    def __repr__(self):
        return f'Fags({self.fag_name})'


class Students(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    fags_id = db.Column(db.Integer, db.ForeignKey('fags.id_'), nullable=False)

    def __repr__(self):
        return f'Students({self.name}, {self.last_name})'
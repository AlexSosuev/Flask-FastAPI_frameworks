# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию. Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = [
    User(id=1, name="Алиса", email="alice@google.com", password="123456"),
    User(id=2, name="Борис", email="boris@bk.ru", password="987654"),
    User(id=3, name="Саша", email="sasha@mail.ru", password="123456S"),
    User(id=4, name="Маша", email="masha@rambler.ru", password="987654M")
]

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_users(request: Request):
    return templates.TemplateResponse("./seminar_5/templates/users.html", {"request": request, "users": users})

if __name__ == "__main__":
    uvicorn.run("homework:app", host="127.0.0.1", port=8080)
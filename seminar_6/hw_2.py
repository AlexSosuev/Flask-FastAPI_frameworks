# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей. Пользователь должен иметь
# следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)

# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения пользователей.

from datetime import datetime
from typing import List
import databases 
import sqlalchemy 
from fastapi import FastAPI 
from pydantic import BaseModel, EmailStr, Field
import uvicorn 

DATABASE_URL = "sqlite:///task_2.db" 
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData() 

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("birthdate", sqlalchemy.String(15)),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
    sqlalchemy.Column("adress", sqlalchemy.String(100))
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

class User(BaseModel):
    firstname:str = Field(title='FirstName', min_length=2)
    lastname:str = Field(title='LastName', min_length=2)
    birthdate:str = Field(title='Birthday')
    email:EmailStr = Field(title='Email', max_length=50)
    adress:str = Field(title='Adress')

class User_with_id(User):
    user_id:int = Field(title='id')


# Функция для создания N фейковых пользователей
@app.post("/fake_users/{count}") 
async def create_note(count: int): 
    for i in range(count): 
        query = users.insert().values(firstname=f'first_name{i}', lastname=f'last_name{i}', email=f'mail{i}@mail.ru', birthdate=f'Data{i}', adress=f'adress{i}') 
        await database.execute(query) 
    return {'message': f'{count} fake users create'}

@app.get("/users/", response_model=List[User_with_id])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)

@app.post("/users/", response_model=User_with_id)
async def create_user(user: User):
    query = users.insert().values(firstname=user.firstname, lastname=user.lastname, email=user.email, birthdate=user.birthdate, adress=user.adress)
    await database.execute(query)

@app.get("/users/{id}", response_model=User_with_id) 
async def read_user(id: int):
    query = users.select().where(users.c.user_id == id) 
    return await database.fetch_one(query)

@app.put("/users/{id}", response_model=User_with_id)
async def update_user(id: int, new_user: User):
    query = users.update().where(users.c.user_id == id).values(**new_user.dict()) 
    await database.execute(query)
    return {**new_user.dict(), "id": id}

@app.delete("/users/{id}")
async def delete_user(id: int):
    query = users.delete().where(users.c.user_id == id) 
    await database.execute(query)
    return {'message': 'User deleted'}

if __name__ == "__main__":
    uvicorn.run("hw_2:app", host="127.0.0.1", port=8000)
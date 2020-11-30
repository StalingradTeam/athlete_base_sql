#импортируем модули uuid и datetime
import uuid
import datetime

#импортируем sqlalchemy
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.Text)  
    last_name = sa.Column(sa.Text)  
    gender = sa.Column(sa.TEXT)  
    email = sa.Column(sa.Text)  
    birthdate = sa.Column(sa.TEXT)  
    height = sa.Column(sa.FLOAT)  


def connect_db():
    """
    Устанавливаем соединение к базе данных
    """
    #Соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    session = sessionmaker(engine)
    return session()


def request_data():
    """
    Запрашиваем у пользователя данные
    """
    print("Привет! Я запишу твои данные")
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    gender = input("Пол: ")
    email = input("Электронная почта: ")
    birthdate = input("Дата рождения: ")
    height = float(input("Рост: "))
    
    #Создаем нового пользователя
    data = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return data


def main():
    """
    Взаимодействие с пользователем
    """
    session = connect_db()
    data = request_data()
    session.add(data)
    session.commit()
    print('Данные сохранены!')


if __name__ == "__main__":
    main()

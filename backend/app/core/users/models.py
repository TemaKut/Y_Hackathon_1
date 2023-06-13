import string

import sqlalchemy as sa
from fastapi import HTTPException, status
from passlib.hash import bcrypt
from sqlalchemy.orm import validates
from sqlalchemy.sql import func

from app.database.connection import Base
from app.logs.logger import log


class User(Base):
    """ Модель пользователя. """

    __tablename__: str = 'users'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        comment='ID пользователя'
    )
    username = sa.Column(
        sa.String(100),
        nullable=False,
        unique=True,
        comment='Username пользователя (Только английские буквы и цифры)',
    )
    password = sa.Column(
        sa.Text,
        nullable=False,
        comment='Хэш пароля'
    )
    registred_at = sa.Column(
        sa.TIMESTAMP(True),
        nullable=False,
        default=func.now(),
        comment='Время регистрации пользователя.'
    )
    is_active = sa.Column(
        sa.Boolean,
        nullable=False,
        default=True,
        comment='Флаг активен ли пользователь.'
    )

    def verify_password(self, password: str):
        """ Сравнение пароля с его хэшем в БД. """

        if not bcrypt.verify(password, self.password):
            log.error('Incorrect password')

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Incorrect password',
            )

    @validates('username')
    def username_validate(self, key, value: str):
        """ Валидация поля username. """

        if len(value) <= 4:
            log.error('Invalid username by length')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Username have to be longer then 4 symbols',
            )

        for ch in value:

            if ch not in f"{string.ascii_letters}1234567890":
                log.error('Invalid username by symbols')
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    'Username have to contains eng. characters only!',
                )

        return value

    @validates('password')
    def password_validate(self, key, value: str):
        """ Хеширование пароля. """

        if len(value) <= 4:
            log.error('Invalid password by length')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Password have to be longer then 4 symbols',
            )

        return bcrypt.hash(value)

    def __repr__(self) -> str:
        """ Строчное представление пользователя. """
        classname: str = self.__class__.__name__

        return f'{classname}<id={self.id}, username={self.username}>'

from datetime import datetime

from pydantic import BaseModel


class UserRegister(BaseModel):
    """ Схема данных пользователя для регистрации. """

    username: str
    password: str


class UserGetToken(BaseModel):
    """ Схема данных для получения токена пользователя. """

    username: str
    password: str


class UserRepresentstion(BaseModel):
    """ Данные пользователя при ответе сервера. """

    id: int
    username: str
    registred_at: datetime
    is_active: bool

    class Config():
        orm_mode = True


class TokenRepresentation(BaseModel):
    """ Визуализация токена пользователя. """

    token: str
    token_type: str = 'Bearer'

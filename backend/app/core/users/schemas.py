from pydantic import BaseModel


class UserRegister(BaseModel):
    """ Схема данных пользователя для регистрации. """

    username: str
    password: str


class UserGetToken(BaseModel):
    """ Схема данных для получения токена пользователя. """

    username: str
    password: str


class TokenRepresentation(BaseModel):
    """ Визуализация токена пользователя. """

    token: str
    token_type: str = 'Bearer'

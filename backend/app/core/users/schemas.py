from pydantic import BaseModel


class UserRepresentation(BaseModel):
    """ Данные о пользователе при ответе сервера. """

    id: str
    username: str

    class Config:
        orm_mode: bool = True

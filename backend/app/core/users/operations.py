from fastapi import Depends

from app.core.users.crud import UsersCrud
from app.core.users.models import User
from app.core.users.auth import create_token
from app.core.users.schemas import (
    UserRegister,
    TokenRepresentation,
    UserGetToken,
)


class UsersOperations():
    """ Высокоуровневые операции над пользователями. """

    def __init__(self, crud: UsersCrud = Depends()):
        self.crud: UsersCrud = crud

    async def register_user(self, data: UserRegister) -> TokenRepresentation:
        """ Регистрация пользователя. """
        user: User = await self.crud.create_user(data)

        return await create_token(user)

    async def get_token(self, data: UserGetToken) -> TokenRepresentation:
        """ Получить токен пользователя. """
        data: dict = data.dict()
        password: str = data.pop('password')

        # Получить пользователя (Данные без пароля)
        user: user = await self.crud.get_user_by_params(data)

        # Сравнить переданный пароль с его хэшем в БД
        user.verify_password(password)

        return await create_token(user)

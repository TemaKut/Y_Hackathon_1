from fastapi import Depends

from app.core.users.crud import UsersCrud
from app.core.users.schemas import UserRegister, TokenRepresentation
from app.core.users.models import User
from app.core.users.auth import create_token


class UsersOperations():
    """ Высокоуровневые операции над пользователями. """

    def __init__(self, crud: UsersCrud = Depends()):
        self.crud: UsersCrud = crud

    async def register_user(self, data: UserRegister) -> TokenRepresentation:
        """ Регистрация пользователя. """
        user: User = await self.crud.create_user(data)

        return await create_token(user)

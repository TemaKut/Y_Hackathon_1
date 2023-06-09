from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.connection import get_async_session
from app.core.users.schemas import UserRegister
from app.core.users.models import User
from app.logs.logger import log


class UsersCrud():
    """ Взаимодействие пользователей с БД. """

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session: AsyncSession = session

    async def create_user(self, data: UserRegister) -> User:
        """ Создать пользователя. """
        user: User = User(**data.dict())

        try:
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)

        except IntegrityError as e:
            log.error(f'User alredy exists {e}')
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'User alredy exists',
            )

        return user

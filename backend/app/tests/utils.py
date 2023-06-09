from functools import wraps

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.users.models import User
from app.tests.conftest import Session


def add_session_in_params(function):
    """ Декоратор. Добавляет объект сессии БД в аргументы """

    @wraps(function)
    async def wrapper(*args, **kwargs):
        """ Обёртка функции. """
        db_sesion: AsyncSession = Session()
        result: any = await function(db_sesion, *args, **kwargs)
        await db_sesion.close()

        return result

    return wrapper


@add_session_in_params
async def get_user_from_db(session, user_data: dict) -> bool:
    """ Проверить есть ли пользователь в БД. """
    query = select(User).filter_by(**user_data)
    result = await session.execute(query)

    user: User = result.scalars().unique().first()

    return user


@add_session_in_params
async def create_user(session, data: dict) -> User:
    """ Создать пользователя напрямую через БД. """
    new_user: User = User(**data)

    session.add(new_user)

    await session.commit()
    await session.refresh(new_user)

    return new_user

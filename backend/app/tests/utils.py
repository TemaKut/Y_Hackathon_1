from copy import deepcopy
from functools import wraps

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select
from sqlalchemy.exc import NoResultFound, IntegrityError

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
async def get_user_from_db(session, data: dict) -> bool:
    """ Проверить есть ли пользователь в БД. """
    data: dict = deepcopy(data)
    if data.get('password'):
        data.pop('password')

    try:
        query: Select = select(User).filter_by(**data)
        result = await session.execute(query)
        user: User = result.scalar_one()

    except NoResultFound:
        assert False, 'User not found'

    return user


@add_session_in_params
async def create_user(session, data: dict) -> User:
    """ Создать пользователя напрямую через БД. """

    try:
        new_user: User = User(**data)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

    except IntegrityError:
        assert False, 'Userr not created'

    return new_user


async def create_and_check_user(data: dict) -> User:
    """ Создать пользователя в БД и проверить появился ли он в БД. """
    await create_user(data)

    return await get_user_from_db(data)

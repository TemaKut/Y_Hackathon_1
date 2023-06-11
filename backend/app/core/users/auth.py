from datetime import datetime, timedelta

from fastapi import Request, Depends, status, HTTPException
from jose import jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.users.models import User
from app.core.users.schemas import TokenRepresentation
from app.settings import SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_MIN
from app.database.connection import get_async_session
from app.logs.logger import log


async def create_token(user: User) -> TokenRepresentation:
    """ Создать токен для пользователя. """
    assert isinstance(user, User), 'Not a User class'

    now: datetime = datetime.utcnow()
    data: dict = {
        "iat": now,
        "exp": now + timedelta(minutes=JWT_EXPIRE_MIN),
        'user_id': user.id,
    }

    # Кодирование данных в токен
    token: str = jwt.encode(
        data,
        key=SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )

    return TokenRepresentation(token=token)


async def get_current_user(
    request: Request,
    session: AsyncSession = Depends(get_async_session),
) -> User:
    """ Получить объект пользователя из БД, выполневшего запрос. """
    error = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Not authorized.')

    # Получение токена авторизации из запроса
    try:
        token: str = request._headers.get('authorization').split(' ')[1]
        token_data: dict = jwt.decode(token, SECRET_KEY, [JWT_ALGORITHM])

    except Exception as e:
        log.error(f'Invalid token {e}')
        raise error

    try:
        user_id: int = token_data['user_id']

        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user: User = result.scalars().first()

        if not user:
            raise

    except Exception as e:
        log.error(f'Cant get user from DB {e}')
        raise error

    return user

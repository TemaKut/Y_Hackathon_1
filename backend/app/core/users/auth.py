from datetime import datetime, timedelta

from jose import jwt

from app.core.users.models import User
from app.core.users.schemas import TokenRepresentation
from app.settings import SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_MIN
# from app.logs.logger import log


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

from fastapi import Request, HTTPException, status

from app.external.storage import StorageYM
from app.logs.logger import log


async def get_current_user(request: Request) -> dict:
    """ Получить объект пользователя, выполневшего запрос отвервера YM. """
    error: HTTPException = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        'Not authorized.',
    )

    # Получение токена авторизации из хедеров запроса
    try:
        token: str = request._headers.get('authorization').split(' ')[1]

    except Exception as e:
        log.error(f'Token not in headers. {e}')
        raise error

    storage: StorageYM = StorageYM()
    user: dict = await storage.get_current_user_from_ym(token)

    return user

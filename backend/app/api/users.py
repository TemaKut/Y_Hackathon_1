from fastapi import APIRouter, Depends

from app.core.users.auth import get_current_user
from app.core.users.schemas import UserRepresentation


users_router = APIRouter(prefix='/users', tags=['Users'])


@users_router.get(
    '/me',
    response_model=UserRepresentation,
    responses={
        401: {'description': 'Error with token (Anauthorized)'},
        503: {'description': 'YM server unaviable.'},
    }
)
async def get_info_about_me(user: dict = Depends(get_current_user)):
    """ Получить информацию о текущем пользователе. """

    return user

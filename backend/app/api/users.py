from fastapi import APIRouter, Body, Depends

from app.core.users.operations import UsersOperations
from app.core.users.auth import get_current_user
from app.core.users.models import User
from app.core.users.schemas import (
    UserRegister,
    UserRepresentstion,
    TokenRepresentation,
    UserGetToken,
)


users_router: APIRouter = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@users_router.post(
    '/register',
    response_model=TokenRepresentation,
    responses={
        400: {'description': 'User alredy exists'},
    },
)
async def register_user(
    data: UserRegister = Body(),
    operations: UsersOperations = Depends(),
):
    """ Регистрация пользователя с получением токена. """

    return await operations.register_user(data)


@users_router.post(
    '/get-token',
    response_model=TokenRepresentation,
    responses={
        404: {'description': 'User not found'},
        400: {'description': 'Incorrect password'},
    },
)
async def get_token(
    data: UserGetToken = Body(),
    operations: UsersOperations = Depends(),
):
    """ Получить токен пользователя. """

    return await operations.get_token(data)


@users_router.get(
    '/me',
    response_model=UserRepresentstion,
)
async def get_info_about_me(user: User = Depends(get_current_user)):
    """ Получить информацию о пользователе, сделавшем запрос. """

    return user

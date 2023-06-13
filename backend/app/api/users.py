from fastapi import APIRouter, Body, Depends

from app.core.users.operations import UsersOperations
from app.core.users.schemas import (
    TokenRepresentation,
    UserGetToken,
    UserRegister
)


users_router: APIRouter = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@users_router.post(
    '/register',
    response_model=TokenRepresentation,
    responses={
        400: {'description': 'User already exists'},
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


@users_router.get('/me')
async def get_info_about_me():
    """ Получить информацию о пользователе, сделавшем запрос. """

    # TODO: Доделать получение пользователя из параметров и формат отдачи
    return 1

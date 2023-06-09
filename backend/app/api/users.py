from fastapi import APIRouter, Body, Depends

from app.core.users.schemas import UserRegister, TokenRepresentation
from app.core.users.operations import UsersOperations


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
    """ Регистрация пользователя. """

    return await operations.register_user(data)

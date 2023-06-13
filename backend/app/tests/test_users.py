import json

import pytest
from httpx import Response, AsyncClient
from fastapi import status

from app.main import app
from app.tests.utils import create_and_check_user


@pytest.mark.parametrize(
    'data, code',
    [
        (
            {
                'username': 'Artemka123',
                'password': 'superlongpass',
            },
            status.HTTP_200_OK,
        ),
        (
            {},
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ),
        (
            {
                'username': '',
                'password': 'superlongpass',
            },
            status.HTTP_400_BAD_REQUEST,
        ),
        (
            {
                'username': 'Artemka123',
                'password': '',
            },
            status.HTTP_400_BAD_REQUEST,
        ),
    ],
)
async def test_register_user(client: AsyncClient, data: dict, code: int):
    """ Регистрация пользователя. """
    url: str = app.url_path_for('register_user')

    response: Response = await client.post(url, json=data)
    assert response.status_code == code


async def test_get_token_after_register(client: AsyncClient):
    """ Получение токена сразу после регистрации. """
    url: str = app.url_path_for('register_user')
    data: dict = {
        'username': 'Artemka123',
        'password': 'superlongpass',
    }

    response: Response = await client.post(url, json=data)
    assert response.status_code == status.HTTP_200_OK

    response_data: dict = json.loads(response.text)
    assert response_data.get('token') and response_data.get('token_type')


@pytest.mark.parametrize(
    'login_data, code',
    [
        (
            {
                "username": "someusername",
                "password": "somepassword",
            },
            status.HTTP_200_OK,
        ),
        (
            {},
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ),
        (
            {
                "username": "notexistingusername",
                "password": "somepassword",
            },
            status.HTTP_404_NOT_FOUND,
        ),
        (
            {
                "username": "someusername",
                "password": "notrealpassword",
            },
            status.HTTP_400_BAD_REQUEST,
        ),
    ],
)
async def test_get_token_for_registred_user(
    client: AsyncClient,
    login_data: dict,
    code: int,
):
    """ Эндпоинт получения токена пользователя. """
    url: str = app.url_path_for('get_token')
    user_data: dict = {
        "username": "someusername",
        "password": "somepassword",
    }

    # Создать пользователя в БД
    await create_and_check_user(user_data)

    # Получить токен при помощи данных пользователя
    response: Response = await client.post(url, json=login_data)

    assert response.status_code == code

    if response.status_code == status.HTTP_200_OK:
        response_data: dict = json.loads(response.text)

        assert response_data.get('token') and response_data.get('token_type')

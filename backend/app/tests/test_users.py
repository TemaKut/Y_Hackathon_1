import json

import pytest
from httpx import Response, AsyncClient
from fastapi import status

from app.main import app


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
async def test_register_user(client: AsyncClient, data, code):
    """ Регистрация пользователя """
    url: str = app.url_path_for('register_user')

    response: Response = await client.post(url, json=data)
    assert response.status_code == code


async def test_get_token_after_register(client):
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

import json

import pytest
from httpx import Response, AsyncClient
from fastapi import status

from app.main import app


@pytest.mark.parametrize(
    'token, code',
    [
        ('Bearer sometoken', status.HTTP_200_OK),
        ('', status.HTTP_401_UNAUTHORIZED),
    ],
)
async def test_200_get_user_data(client: AsyncClient, token: str, code: int):
    """ Статус 200 при запросе текущего пользователя с токеном. """
    url: str = app.url_path_for('users_me')
    headers: dict = {'Authorization': token}

    response: Response = await client.get(url, headers=headers)

    assert response.status_code == code

    if code == status.HTTP_200_OK:
        response_data: dict = json.loads(response.text)
        assert response_data.get('id') and response_data.get('username')

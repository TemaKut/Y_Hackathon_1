import json

from httpx import Response
from fastapi import status

from app.main import app


async def test_401_get_user_data_without_token(client):
    """ Ошибка 401 при запросе пользователя без токена. """
    url: str = app.url_path_for('users_me')
    response: Response = await client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_200_get_user_data(client):
    """ Статус 200 при запросе текущего пользователя с токеном. """
    url: str = app.url_path_for('users_me')
    headers: dict = {'Authorization': 'Bearer sometoken'}

    response: Response = await client.get(url, headers=headers)

    assert response.status_code == status.HTTP_200_OK

    response_data: dict = json.loads(response.text)
    assert response_data.get('id') and response_data.get('username')

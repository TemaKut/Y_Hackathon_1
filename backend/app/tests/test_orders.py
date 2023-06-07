import json

from httpx import Response
from fastapi import status

from app.main import app


async def test_get_detailed_products_in_order(client):
    """ Тест эндпоинта для успешного получения продуктов из заказа. """
    orderkey: str = '46c39f23ec7f3e6ba6776d01c7edb4b9'
    url: str = app.url_path_for(
        'get_products_of_order',
        orderkey=orderkey,
    )

    response: Response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.text)


async def test_detailed_products_in_order_with_nonexisting_orderkey(client):
    """
    Проверка ошибок при получении продуктов заказа с несуществующим orderkey
    """
    orderkey: str = 'nonexistingorderkey'
    url: str = app.url_path_for(
        'get_products_of_order',
        orderkey=orderkey,
    )

    response: Response = await client.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

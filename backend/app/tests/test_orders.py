import json

import pytest
from fastapi import status
from httpx import AsyncClient, Response

from app.main import app


async def test_get_detailed_products_in_order(client: AsyncClient):
    """ Тест эндпоинта для успешного получения продуктов из заказа. """
    orderkey: str = '46c39f23ec7f3e6ba6776d01c7edb4b9'
    url: str = app.url_path_for(
        'get_products_of_order',
        orderkey=orderkey,
    )

    response: Response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.text)


async def test_detailed_products_in_order_with_nonexisting_orderkey(
    client: AsyncClient,
):
    """ Проверка ошибок при получении продуктов заказа. """
    orderkey: str = 'nonexistingorderkey'
    url: str = app.url_path_for(
        'get_products_of_order',
        orderkey=orderkey,
    )

    response: Response = await client.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize(
    'orderkey, sku, code, is_in',
    [
        (
            '0f489755c658e890bfd405327298525d',
            'a44fc222facab5bdffdfb2e870fb5abb',
            status.HTTP_200_OK,
            True,
        ),
        (
            'nonexistingorderkey',
            'a44fc222facab5bdffdfb2e870fb5abb',
            status.HTTP_400_BAD_REQUEST,
            False,
        ),
        (
            '0f489755c658e890bfd405327298525d',
            'skunotinorder',
            status.HTTP_200_OK,
            False,
        ),
    ]
)
async def test_is_sku_in_order(
    client: AsyncClient,
    orderkey: str,
    sku: str,
    code: int,
    is_in: bool
):
    """ Проверка корректности получения ответа есть ли sku в заказе. """
    url: str = app.url_path_for(
        'is_sku_in_order',
        orderkey=orderkey,
        sku=sku,
    )
    response: Response = await client.get(url)

    assert response.status_code == code

    if response.status_code == status.HTTP_200_OK:
        response_data: bool = json.loads(response.text)

        assert isinstance(response_data, bool)
        assert response_data is is_in

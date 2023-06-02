import json

from httpx import AsyncClient

from app.settings import YM_DOMAIN


class StorageYM():
    """ Взаимодействие с эндпоинтами Яндекс маркета """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.YM_DOMAIN = YM_DOMAIN

    async def get_product_by_sku(self, sku: str) -> dict | None:
        """ Запрос на получение товара по его SKU на склад ЯМ. """
        url = f'{self.YM_DOMAIN}/product/{sku}'

        async with AsyncClient() as client:
            response = await client.get(url, timeout=1000)

        return json.loads(response.text)

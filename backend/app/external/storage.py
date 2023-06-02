import json

from fastapi import HTTPException, status
from httpx import AsyncClient

from app.settings import YM_DOMAIN
from app.logs.logger import log


class StorageYM():
    """ Взаимодействие с эндпоинтами Яндекс маркета """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.YM_DOMAIN = YM_DOMAIN

    async def get_product_by_sku(self, sku: str) -> dict | None:
        """ Запрос на получение товара по его SKU на склад ЯМ. """
        url = f'{self.YM_DOMAIN}/product/{sku}'

        async with AsyncClient() as client:

            try:
                response = await client.get(url, timeout=1000)

            except Exception as e:
                log.critical(e)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail='Fatal request to YM server'
                )

        return json.loads(response.text)

    async def get_product_cargotype(self, sku: str) -> list:
        """ Получить список карготипов продукта. """
        url = f'{self.YM_DOMAIN}/product/{sku}/cargotypes'

        async with AsyncClient() as client:

            try:
                response = await client.get(url, timeout=1000)

            except Exception as e:
                log.critical(e)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail='Fatal request to YM server'
                )

        return json.loads(response.text)

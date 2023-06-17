import json

from fastapi import HTTPException, status
from httpx import AsyncClient, Response

from app.settings import YM_DOMAIN
from app.logs.logger import log


class StorageYM():
    """ Взаимодействие с внешними сервисами Яндекс маркета """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.YM_DOMAIN = YM_DOMAIN

    async def get_cell_to_work(self) -> dict[str, str]:
        """ Получить очередную ячейку с orderkey """
        url: str = f'{self.YM_DOMAIN}/cell-to-work'

        async with AsyncClient() as client:

            try:
                response: Response = await client.get(url)
                response: dict = json.loads(response.text)

            except Exception as e:
                log.critical(f'Error get cell from YM server {e}')
                raise HTTPException(
                    status.HTTP_503_SERVICE_UNAVAILABLE,
                    'Error with get cell from YM server',
                )

        return response

    async def get_cargotypes_for_skus(self, skus: list[str]) -> list[dict]:
        """ Получить список крготипов для кадого из sku """
        url: str = f'{self.YM_DOMAIN}/sku/cargotypes'

        async with AsyncClient() as client:

            try:
                response: Response = await client.post(url, json=skus)
                cargotypes: list[dict] = json.loads(response.text)

            except Exception as e:
                log.critical(f'Error get sku cargotypes from YM server {e}')
                raise HTTPException(
                    status.HTTP_503_SERVICE_UNAVAILABLE,
                    'Error with get sku cargotypes from YM server',
                )

        if not cargotypes:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'C.T. not found')

        return cargotypes

    async def get_sizes_for_skus(self, skus: list[str]) -> list[dict]:
        """ Получить список с расширенной информацией о skus (Их размер) """
        url: str = f'{self.YM_DOMAIN}/sku/'

        async with AsyncClient() as client:

            try:
                response: Response = await client.post(url, json=skus)
                sizes: list[dict] = json.loads(response.text)

            except Exception as e:
                log.critical(f'Error with get sku sizes from YM server {e}')
                raise HTTPException(
                    status.HTTP_503_SERVICE_UNAVAILABLE,
                    'Error with get sku sizes from YM server',
                )

        if not sizes:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Sizes not found')

        return sizes

    async def get_list_of_order(self, orderkey: str) -> list[dict] | list:
        """ Получить список записей о заказе от сервера YM """
        url: str = f'{self.YM_DOMAIN}/orders/{orderkey}'

        async with AsyncClient() as client:

            try:
                response: Response = await client.get(url)
                orders = json.loads(response.text)

            except Exception as e:
                log.critical(f'Error with get order from YM server {e}')
                raise HTTPException(
                    status.HTTP_503_SERVICE_UNAVAILABLE,
                    'Error with get order from YM server',
                )

        if not orders:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Order not found')

        return orders

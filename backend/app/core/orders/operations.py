import asyncio

from fastapi import HTTPException, status

from app.external.storage import StorageYM
from app.logs.logger import log


class OrdersOperations():
    """ Высокоуровневые операции над заказами. """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.storage_ym = StorageYM()

    async def get_info_about_order(self, orderkey: str) -> dict:
        """ Получить обогощённую информацию о заказе. """
        # Получить заказ и компактизировать его до уникальных значений
        order_multi: list = await self.storage_ym.get_list_of_order(orderkey)
        unique_products: list = await self._to_unique_products(order_multi)
        size_cargo: dict = await self.get_size_and_cargo_for_products(
            unique_products,
        )
        print(size_cargo)

    async def get_size_and_cargo_for_products(self, products: list) -> dict:
        """
        Из уникальных продуктов выбрать skus для дальнейших запросов
        и асинхронно сделать запросы на получение размеров и карготипов
        """
        unique_skus: list = []
        for product in products:

            if sku := product.get('sku'):
                unique_skus.append(sku)

        return await self._get_size_and_cargotype_for_skus(unique_skus)

    async def _get_size_and_cargotype_for_skus(self, skus: list[str]) -> dict:
        """
        Сделать асинхронный запрос на 2 url
        для получения размеров и карготипов для sku
        """
        tasks: list = [
            self.storage_ym.get_sizes_for_skus(skus),
            self.storage_ym.get_cargotypes_for_skus(skus),
        ]

        sizes, cargotypes = await asyncio.gather(*tasks)

        return {'sizes': sizes, 'cargotypes': cargotypes}

    async def _to_unique_products(self, order_multi: list) -> list:
        """ Разделить список не уникальных товаров в заказе на уникальные """

        if not order_multi:
            log.error('Not products in oder')
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Not products')

        unique_products: dict = {}

        for product in order_multi:
            sku: str = product.get('sku')

            if unique_product := unique_products.get(sku):
                unique_product['count'] += 1

            else:
                unique_products[sku] = product | {'count': 1}

        return list(unique_products.values())

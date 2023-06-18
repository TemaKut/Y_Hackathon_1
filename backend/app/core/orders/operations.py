import asyncio

from fastapi import HTTPException, status

from app.external.storage import StorageYM
from app.logs.logger import log


class OrdersOperations():
    """ Высокоуровневые операции над заказами. """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.storage_ym = StorageYM()

    async def get_order_products(self, orderkey: str) -> list[dict]:
        """ Получить обогащённую информацию о товарах в заказе. """
        # Получить заказ и компактизировать его до уникальных значений
        order_multi: list = await self.storage_ym.get_list_of_order(orderkey)
        unique_products: dict = await self._to_unique_products(order_multi)

        # Запросить сопутствующую информацию к каждому из уникальных товаров
        size_cargo: dict = await self._get_size_and_cargo_for_products(
            list(unique_products.values()),
        )

        # Добавить размеры для каждого уз уникальных товаров (Мутация объекта)
        for sizes in size_cargo.get('sizes'):
            sku: str = sizes.get('sku')
            unique_products[sku] = unique_products[sku] | sizes

        # Добавить карготипы к уникальным продуктам (Мутация объекта)
        for cargo in size_cargo.get('cargotypes'):
            sku: str = cargo.get('sku')
            cargotype: list = [cargo.get('cargotype')]
            product: dict = unique_products[sku]

            if product.get('cargotypes'):
                product['cargotypes'] += cargotype

            else:
                product['cargotypes'] = cargotype

        return list(unique_products.values())

    async def is_sku_in_order(self, orderkey: str, sku: str) -> bool:
        """ Есть ли sku в конкретном заказе. """
        all_products: list = await self.storage_ym.get_list_of_order(orderkey)

        for product in all_products:
            product_sku: str = product.get('sku')

            if sku == product_sku:

                return True

        return False

    async def _get_size_and_cargo_for_products(self, products: list) -> dict:
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

    async def _to_unique_products(self, order_multi: list) -> dict:
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

        return unique_products

import asyncio

from fastapi import HTTPException, status

from app.core.orders.schemas import ProductSKU
from app.external.storage import StorageYM
from app.logs.logger import log


class OrdersOperations():
    """ Высокоуровневые операции над заказами. """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.storage_ym = StorageYM()

    async def predict_packaging(self, data: list[ProductSKU]): 
        """ Предсказать распределение товаров по пакетам. """
        valid_data = await self.get_products_from_ym(data)
        print(valid_data)

    async def get_products_from_ym(self, data: list[ProductSKU]) -> list:
        """ Получить товары по sku c сервера YM. (Асинхронно)"""
        products = []
        _used_skus = []

        # Создать задачи для асинхронного получения описания товаров
        tasks = []

        for product in data:
            sku = product.sku

            if sku in _used_skus:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail={
                        'description': 'Two or more same sku',
                        'fail_skus': sku,
                    }
                )

            task = self.__check_sku(products, sku)

            tasks.append(task)
            _used_skus.append(sku)

        # Запустить асинхронные запросы для получения sku
        await asyncio.gather(*tasks)

        # Создать и запустить асинхронные задачи для добавления карготипов
        tasks = []

        for product in products:
            task = self.__add_cargotypes_to_result(product)
            tasks.append(task)

        await asyncio.gather(*tasks)

        return products

    async def __add_cargotypes_to_result(self, product: dict) -> None:
        """ Добавить в словарь продукта список карготипов. """
        try:
            sku = product['sku']

        except Exception as e:
            log.critical(f'Product does not hawe "sku" {e}')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Product does not hawe "sku"'
            )

        cargotypes = await self.storage_ym.get_product_cargotype(sku)
        product['cargotypes'] = cargotypes

    async def __check_sku(self, products: list, sku: str) -> None:
        """ При помощи запроса к серверу ЯМ выяснить есть ли продукт с sku """
        prod = await self.storage_ym.get_product_by_sku(sku=sku)

        if not prod:
            log.error(f'Product {sku} not exists in storage')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'description': 'Product not exists in storage',
                    'sku': sku,
                },
            )

        products.append(prod)

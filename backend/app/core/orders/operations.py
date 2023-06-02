import asyncio

from fastapi import HTTPException, status

from app.core.orders.schemas import ProductSKU
from app.external.storage import StorageYM


class OrdersOperations():
    """ Высокоуровневые операции над заказами. """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.storage_ym = StorageYM()

    async def predict_packaging(self, data: list[ProductSKU]):
        """ Предсказать распределение товаров по пакетам. """
        # valid_data = await self._check_skus(data)  # TODO: Раскоментить 

    async def _check_skus(self, data: list[ProductSKU]) -> list:
        """ Сверить наличие товара на складе. """
        result = []
        tasks = []

        for product in data:
            task = self.__check_sku(result, product.sku)
            tasks.append(task)

        await asyncio.gather(*tasks)

        return result

    async def __check_sku(self, result: list, sku: str) -> None:
        """ При помощи запроса к серверу ЯМ выяснить есть ли продукт с sku """
        prod = await self.storage_ym.get_product_by_sku(sku=sku)

        if not prod:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'description': 'Product not exists in storage',
                    'sku': sku,
                },
            )

        result.append(prod)

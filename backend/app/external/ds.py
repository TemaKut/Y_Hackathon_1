from httpx import AsyncClient, Response

from app.core.orders.operations import OrdersOperations
from app.settings import DS_DOMAIN


class DsAPI():
    """
    Взаимодействие с внешним сервисом Data Science посредством его api
    """

    def __init__(self):
        self.orders_operations: OrdersOperations = OrdersOperations()
        self.DS_DOMAIN: str = DS_DOMAIN

    async def predict_package(self, orderkey: str):
        """ Предсказать упаковку для заказа. """
        url: str = f'{self.DS_DOMAIN}/api/v1/order/model/predict'
        products: list = await self.orders_operations.get_order_products(
            orderkey,
        )

        async with AsyncClient() as client:
            response: Response = await client.post(url, json=products)
            print(response)
            # TODO: После того как DS закончат работать - доработать их ответ

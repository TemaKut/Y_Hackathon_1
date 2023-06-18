import json

from httpx import AsyncClient, Response
from fastapi import HTTPException, status

from app.core.orders.operations import OrdersOperations
from app.settings import DS_DOMAIN
from app.logs.logger import log


class DsAPI():
    """
    Взаимодействие с внешним сервисом Data Science посредством его api
    """

    def __init__(self):
        self.orders_operations: OrdersOperations = OrdersOperations()
        self.DS_DOMAIN: str = DS_DOMAIN

    async def predict_package(self, orderkey: str):
        """ Предсказать упаковку для заказа. """
        url: str = f'{self.DS_DOMAIN}/api/v1/predict'
        products: list = await self.orders_operations.get_order_products(
            orderkey,
        )

        async with AsyncClient() as client:

            try:
                response: Response = await client.post(url, json=products)
                response: dict = json.loads(response.text)

            except Exception as e:
                log.error(f'Fail response from ds predict {e}')
                raise HTTPException(
                    status.HTTP_503_SERVICE_UNAVAILABLE,
                    'Fail response from ds predict',
                )

        return response

from fastapi import APIRouter, Body, Depends

from app.core.orders.schemas import ProductSKU
from app.core.orders.operations import OrdersOperations


orders_router = APIRouter(
    prefix='/orders',
    tags=['Заказы']
)


@orders_router.post(
    '/predict',
)
async def test(
    data: list[ProductSKU] = Body(),
    operations: OrdersOperations = Depends(),
):
    """ Предсказать распределение товаров по упаковкам. """
    await operations.predict_packaging(data)

    return 1

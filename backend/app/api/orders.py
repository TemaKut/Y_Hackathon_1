from fastapi import APIRouter, Depends

from app.external.ds import DsAPI
from app.core.orders.operations import OrdersOperations
from app.core.orders.schemas import Product


orders_router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


@orders_router.get(
    '/{orderkey}',
    name='get_products_of_order',
    response_model=list[Product],
)
async def get_products_of_order(
    orderkey: str,
    operations: OrdersOperations = Depends(),
):
    """ Получить список продуктов, которые принадлежать заказу с orderkey """

    return await operations.get_order_products(orderkey)


@orders_router.get(
    '/{orderkey}/predict',
    responses={
        400: {'description': 'Incorrect orderkey or another data'},
        503: {'description': 'YM server unaviable.'},
    }
)
async def predict_package_by_orderkey(
    orderkey: str,
    ds_api: DsAPI = Depends(),
):
    """ Предсказать упаковку(и) для заказа. """
    await ds_api.predict_package(orderkey)
    # TODO: После того как DS доделают модель - отдать результат
    return 1

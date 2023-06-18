from fastapi import APIRouter, Depends

from app.external.ds import DsAPI
from app.external.storage import StorageYM
from app.core.orders.operations import OrdersOperations
from app.core.orders.schemas import Product


orders_router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


@orders_router.get('/cell-to-work')
async def get_cell_to_work(storage: StorageYM = Depends()):
    """ Получить ячейку к работе. """

    return await storage.get_cell_to_work()


@orders_router.get(
    '/{orderkey}',
    name='get_products_of_order',
    response_model=list[Product],
    responses={
        400: {'description': 'Incorrect orderkey or another data'},
        503: {'description': 'YM server unaviable.'},
    },
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
    },
)
async def predict_package_by_orderkey(
    orderkey: str,
    ds_api: DsAPI = Depends(),
):
    """ Предсказать упаковку(и) для заказа. """

    return await ds_api.predict_package(orderkey)


@orders_router.get(
    '/{orderkey}/products/{sku}/validate',
    name='is_sku_in_order',
    response_model=bool,
    responses={
        400: {'description': 'Incorrect orderkey'},
    },
)
async def is_sku_in_order(
    orderkey: str,
    sku: str,
    operations: OrdersOperations = Depends(),
):
    """ Есть ли sku в составе заказа. """

    return await operations.is_sku_in_order(orderkey, sku)

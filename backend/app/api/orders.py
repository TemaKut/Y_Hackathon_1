from fastapi import APIRouter, Depends

from app.external.ds import DsAPI


orders_router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


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

    return 1

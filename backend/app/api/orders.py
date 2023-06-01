from fastapi import APIRouter


orders_router = APIRouter(
    prefix='/orders',
    tags=['Заказы']
)


@orders_router.get('/')
async def test():
    """ Тестовый роут. """

    return 'test'

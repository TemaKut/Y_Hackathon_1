from fastapi import FastAPI, Body, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from app.data.orders import orders_data
from app. data.orders_boxes import orders_boxes
from app.data.sku import sku_data
from app.data.cargotypes import cargotypes_data
from app.schemas import TokenData


app = FastAPI(
    title='Mock server (Yandex db)',
    description="""
        Простой сервер с моками отдаваемых данных от сервера склада ЯМ.
        Для моков использована маленькая часть из представленных csv данных
        Данные хранятся в .py файлах, в структурах, приближенным к ответам
        базы данных MongoDB. .py файлы используются с целью изменений данных
        без необходимости создавать лишнюю БД
    """,
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/users/me')
async def get_info_about_user(data: TokenData = Body()):
    """
    Возвращает краткую информацию о пользователе.
    Предполагается что аккаунт сотрудников Яндекса един для всей экосистемы.
    """

    # Какие-то суперсложные манипуляции с токеном из data..

    return {'id': 'SuperLooongestUserId123', 'username': 'ArtemKutuzov'}


@app.get('/orders/{orderkey}')
async def get_order_by_orderkey(orderkey: str):
    """
    Найти и вернуть запись по её orderkey. В ответе список заказа.
    различие в sku.
    """
    result: list = []

    for order in orders_data:

        if order.get('orderkey') == orderkey:
            result.append(order)

    return result


@app.patch('/orders/{orderkey}')
async def update_of_order(orderkey: str, data: dict = Body()):
    """ Частично обновить заказ. """
    valid_keys_to_update: list[str] = ['who']

    for key in data.keys():

        if key not in valid_keys_to_update:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Not valid key')

    result: list = []

    for order in orders_data:

        if order.get('orderkey') != orderkey:
            print(1)
            continue

        for key, value in data.items():
            print(2)
            order[key] = value
            result.append(order)

    return result


@app.post('/sku/')
async def get_a_list_of_sku(data: list[str] = Body()):
    """ Получить список sku (Расширенный) """
    result: list = []

    for sku in sku_data:

        if sku.get('sku') in data:
            result.append(sku)

    return result


@app.post('/sku/cargotypes')
async def get_a_list_of_cargotypes(data: list[str]):
    """ Получить спискок карготипов для каждого sku """
    result: list = []

    for cargotype in cargotypes_data:

        if cargotype.get('sku') in data:

            result.append(cargotype)

    return result


@app.get('/boxs/{box_num}')
async def get_order_by_box_num(box_num: str) -> str:
    """ Найти и вернуть номер заказа по номеру ячейки. """

    if box_num not in orders_boxes:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Not found')
    else:
        return orders_boxes[box_num]

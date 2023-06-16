import os
import random

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.data.orders import orders_data
from app.data.sku import sku_data
from app.data.cargotypes import cargotypes_data


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

# Статические файлы
static_dir: str = os.path.join('app/', 'static')
app.mount('/static', StaticFiles(directory=static_dir), name='static')


@app.get('/cell-to-work')
async def get_cell_to_work():
    """ Получить нужную ячейку к работе. """

    cell_orderkey: dict[str, str] = {
        'ATM-1': 'a763be2ddb7cb12da46be17be5528bee',
        'ATM-2': '1913aa8f0023c18ba8724a234bbc987f',
        'ATM-3': '40c33668fe8dba60a8bb0a982d0a993b',
        'ATM-4': '46c39f23ec7f3e6ba6776d01c7edb4b9',
        'ATM-5': '0f489755c658e890bfd405327298525d',
    }

    cell, orderkey = random.choice(list(cell_orderkey.items()))

    return {'cell': cell, 'orderkey': orderkey}


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

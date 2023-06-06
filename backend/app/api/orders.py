from typing import List

from fastapi import APIRouter
from app.core.orders.schemas import Order, Product

orders_router = APIRouter(
    prefix='/orders',
    tags=['Заказы']
)


@orders_router.get("/{order_id}", response_model=Order)
def get_order(order_id: str):  # TODO: сделать асинхронно?
    order_data = {  # TODO: настроить получение данных
        'box_num': '1',
        'goods_wght': '4.3',
        'orderkey': 'a763be2ddb7cb12da46be17be5528bee',
        'pack_volume': '18480',
        'rec_calc_cube': '40050',
        'recommended_carton': '',
        'sel_calc_cube': '0',
        'selected_carton': '',
        'sku': 'ef7bf24039a47423e252abc269943e2f',
        'trackingid': 'dfad8f14c7d1071b00f2e17c5983aa83',
        'who': '',
        'whs': '0'
    }
    order = Order(**order_data)
    return order


@orders_router.get("/{orderkey}/products",
                   response_model=List[Product])
def get_order_products(orderkey: str):  # TODO: сделать асинхронно?
    products_data = [  # TODO: настроить получение данных
        {
            'sku': '03792096ffa3e48a6124162e1a2d825',
            'logo': 'http://localhost:8000/static/defaultimg.png',
            'name': 'Яндекс станция мини',
            'cargotypes': [50, 13],
            'additionalPackaging': 'Пузырчатая плёнка',
            'userTip': 'Нужно сканировать IMEI',
        }
    ]
    products = [Product(**product_data) for product_data in products_data]
    return products

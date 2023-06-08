from pydantic import BaseModel


class Item(BaseModel):
    """ Схема данных продукта """

    sku: str
    count: int
    a: float
    b: float
    c: float
    goods_wght: float
    cargotypes: list[float]


class OrderFromBackend(BaseModel):
    """ Схема получаемых данных от бэка (Заказ). """

    orderkey: str
    items: list[Item]

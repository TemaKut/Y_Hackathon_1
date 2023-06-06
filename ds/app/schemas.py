from pydantic import BaseModel


class Item(BaseModel):
    """ Схема данных продукта """

    sku: str
    count: int
    size1: float
    size2: float
    size3: float
    weight: float
    cargotypes: list[float]


class OrderFromBackend(BaseModel):
    """ Схема получаемых данных от бэка (Заказ). """

    orderkey: str
    items: list[Item]

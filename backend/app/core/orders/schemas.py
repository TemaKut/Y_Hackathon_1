from pydantic import BaseModel


class Product(BaseModel):
    """ Схема отображаемых данных продукта из заказа. """

    box_num: int
    cell_name: str
    goods_wght: float
    orderkey: str
    pack_volume: int
    rec_calc_cube: int
    sel_calc_cube: int
    sku: str
    trackingid: str
    count: int
    a: float
    b: float
    c: float
    cargotypes: list[int]

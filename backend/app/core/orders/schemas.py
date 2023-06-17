from pydantic import BaseModel, validator

from app.settings import YM_DOMAIN


def f():
    return 'd'


class Product(BaseModel):
    """ Схема отображаемых данных продукта из заказа. """

    box_num: int
    cell_name: str
    goods_wght: float
    orderkey: str
    pack_volume: int
    rec_calc_cube: int
    sel_calc_cube: int
    sku_name: str = None
    sku_logo_url: str = None
    sku: str
    trackingid: str
    count: int
    a: float
    b: float
    c: float
    cargotypes: list[int]

    @validator('sku_logo_url')
    def set_ym_domain(cls, value):
        """ Добавить к sku_logo_url доменное имя сервера YM """

        return f'{YM_DOMAIN}{value}'

from pydantic import BaseModel


class ProductToPredict(BaseModel):
    """ Схема данных продукта перед предсказанием модели. """

<<<<<<< HEAD
    sku: str
    count: int
    a: float
    b: float
    c: float
    goods_wght: float
    cargotypes: list[float]


class OrderFromBackend(BaseModel):
    """ Схема получаемых данных от бэка (Заказ). """

=======
    a: float
    b: float
    box_num: int = None
    c: float
    cargotypes: list[float]
    cell_name: str = None
    count: int
    goods_wght: float
>>>>>>> develop
    orderkey: str
    pack_volume: int
    rec_calc_cube: int
    sel_calc_cube: int
    sku: str = None
    trackingid: str = None

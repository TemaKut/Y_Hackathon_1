from pydantic import BaseModel


class ProductToPredict(BaseModel):
    """ Схема данных продукта перед предсказанием модели. """

    a: float
    b: float
    box_num: int = None
    c: float
    cargotypes: list[int]
    cell_name: str = None
    count: int
    goods_wght: float
    orderkey: str
    pack_volume: int
    rec_calc_cube: int
    sel_calc_cube: int
    sku: str = None
    trackingid: str = None

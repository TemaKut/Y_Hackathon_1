from pydantic import BaseModel


class ProductToPredict(BaseModel):
    """ Схема данных продукта перед предсказанием модели. """

    sku: str
    count: int
    a: float
    b: float
    c: float
    goods_wght: float
    cargotypes: list[float]

from pydantic import BaseModel


class ProductSKU(BaseModel):
    """ Данные товара перед предсказанием. """

    sku: str


class OrdersToRepresentation(BaseModel):
    """ Данные заказа для предоставления в качестве ответа на запрос. """

    class Config:
        orm_mode = True

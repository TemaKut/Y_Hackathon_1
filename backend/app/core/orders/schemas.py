from pydantic import BaseModel


class OrdersBeforePredict(BaseModel):
    """ Данные заказа перед первичным предсказанием модели DS. """

    pass


class OrdersToRepresentation(BaseModel):
    """ Данные заказа для предоставления в качестве ответа на запрос. """

    class Config:
        orm_mode = True

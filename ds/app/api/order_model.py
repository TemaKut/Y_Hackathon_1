# import pickle
from pprint import pprint

from fastapi import APIRouter, Body

from app.schemas import ProductToPredict


order_model_router = APIRouter(
    prefix='/order/model',
    tags=['Модель предсказания упаковки']
)


@order_model_router.post('/predict')
def predict_package_for_order(data: list[ProductToPredict] = Body()):
    """ Предсказать упаковку для заказа. """
    for product in data:
        pprint(product.dict())
    # with open('app/pickle_model/model.pickle', 'rb') as file:
    #     model = pickle.load(file)

    # result = model.predict(data)
    # return result
    return 1

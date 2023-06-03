from fastapi import APIRouter


orders_router = APIRouter(
    prefix='/orders',
    tags=['Заказы']
)

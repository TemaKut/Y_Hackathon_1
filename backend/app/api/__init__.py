from fastapi import APIRouter

from app.api.orders import orders_router


api_router_v1 = APIRouter(prefix='/api/v1')

# Подключение роутов
api_router_v1.include_router(orders_router)

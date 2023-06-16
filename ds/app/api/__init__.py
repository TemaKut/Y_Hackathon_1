from fastapi import APIRouter

from app.api.model import order_model_router


api_router = APIRouter(prefix='/api/v1')

# Подключение роутов
api_router.include_router(order_model_router)

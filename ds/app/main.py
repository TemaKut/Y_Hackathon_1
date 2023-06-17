from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router


app = FastAPI(title='Сервер модели ML')

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключерие роутов
app.include_router(api_router)

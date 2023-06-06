from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router_v1
from app.settings import DEBUG


app = FastAPI(
    debug=DEBUG,
    title='Super backend :)',
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутов
app.include_router(api_router_v1)

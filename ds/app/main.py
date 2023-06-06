from fastapi import FastAPI

from app.api import api_router


app = FastAPI(title='Сервер модели ML')

# Подключерие роутов
app.include_router(api_router)

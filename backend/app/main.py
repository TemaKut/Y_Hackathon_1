from fastapi import FastAPI

from app.api import api_router_v1
from app.settings import DEBUG


app = FastAPI(
    debug=DEBUG,
    title='Super backend :)',
)

# Подключение роутов
app.include_router(api_router_v1)

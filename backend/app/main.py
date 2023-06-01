from fastapi import FastAPI

from app.settings import DEBUG
from app.api import api_router_v1


app = FastAPI(
    debug=DEBUG,
    title='Super backend :)',
)


# Подключение роутов
app.include_router(api_router_v1)

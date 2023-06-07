import asyncio

import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture(scope="session")
def event_loop():
    """ Дополнительный event loop для тестов """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function')
async def client():
    """ Асинхронный клиент для запросов на сервер. """

    async with AsyncClient(app=app, base_url='http://test_url') as client:
        yield client

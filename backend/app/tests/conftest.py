import asyncio

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncSession, AsyncEngine
)
from sqlalchemy.orm import sessionmaker

from app.core.users.models import User
from app.database.connection import get_async_session
from app.main import app
from app.settings import DB_URL_TEST


async_engine: AsyncEngine = create_async_engine(DB_URL_TEST, future=True)

Session: AsyncSession = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@pytest.fixture(scope='session')
def event_loop():
    """ Дополнительный event loop для тестов. """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function')
async def client():
    """ Фикстура создаёт объект клиента приложения fastapi. """

    async def get_async_session_new() -> AsyncSession:
        """ Получить объект асинхронной сессии БД, а следом закрыть её. """
        session = Session

        try:
            yield session

        except Exception:
            await session.rollback()

        finally:
            await session.close()

    app.dependency_overrides[get_async_session] = get_async_session_new

    async with AsyncClient(app=app, base_url="http://test") as client_:
        yield client_


@pytest.fixture(scope='function', autouse=True)
async def setup_db(request):
    """ Создать БД с необходимыми таблицами, а после всех тестов удалить. """
    async with async_engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)

    yield

    async with async_engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.settings import DB_URL
from app.logs.logger import log


# При создании таблицы БД -> наследоваться от этого объекта
Base = declarative_base()

async_engine = create_async_engine(DB_URL, future=True)

# Через объект от Session обращаться к БД
Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    """ Получить объект асинхронной сессии БД, а следом закрыть её. """
    session = Session()

    try:
        yield session

    except Exception as e:
        log.critical(f'Filed with DB session: {e}')
        pass

    finally:
        await session.close()

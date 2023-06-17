from sqlalchemy import text

from app.database.connection import Session


async def test_connect_to_db():
    """ Тестирование подключения к БД. """

    async with Session() as session:

        try:
            await session.execute(text('SELECT 1'))

        except Exception as e:

            assert False, f'Db connection error: {e}'

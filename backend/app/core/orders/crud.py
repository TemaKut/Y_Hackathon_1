from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_async_session


class OrdersCRUD():
    """ Create Read Update Delete операции с заказами в БД. """

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        """ Инициализация объекта класса. """
        self.session = session  # Объект сессии БД

from app.external.storage import StorageYM
from app.core.orders.crud import OrdersCRUD


class OrdersOperations():
    """ Высокоуровневые операции над заказами. """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.storage_ym = StorageYM()
        self.orders_crud = OrdersCRUD()

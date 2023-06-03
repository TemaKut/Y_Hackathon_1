from app.settings import YM_DOMAIN


class StorageYM():
    """ Взаимодействие с внешними сервисами Яндекс маркета """

    def __init__(self):
        """ Инициализация объекта класса. """
        self.YM_DOMAIN = YM_DOMAIN

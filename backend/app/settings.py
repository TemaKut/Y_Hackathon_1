import os
from pathlib import Path

from dotenv import load_dotenv


# __Загрузка данных из окружения__
load_dotenv()

# Корневая директория
BASE_DIR = Path(__file__).resolve().parent

# Режим дебаг приложения
DEBUG = True

# Секретный ключ приложения
SECRET_KEY: str = os.getenv('SECRET_KEY')

# Подключение к БД
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = 'localhost' if DEBUG else os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_URL = (
    "postgresql+asyncpg://"
    + f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Подключение к БД (Для тестирования!)
DB_USER_TEST = os.getenv("DB_USER_TEST")
DB_PASSWORD_TEST = os.getenv("DB_PASSWORD_TEST")
DB_NAME_TEST = os.getenv("DB_NAME_TEST")
DB_HOST_TEST = 'localhost' if DEBUG else os.getenv("DB_HOST_TEST")
DB_PORT_TEST = os.getenv("DB_PORT_TEST")
DB_URL_TEST = (
    "postgresql+asyncpg://"
    + f"{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}"
    + f"/{DB_NAME_TEST}"
)

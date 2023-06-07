import os
from pathlib import Path

from dotenv import load_dotenv


# __Загрузка данных из окружения__
load_dotenv()

# Корневая директория
BASE_DIR: Path = Path(__file__).resolve().parent

# Режим дебаг приложения
DEBUG: bool = True

# Секретный ключ приложения
SECRET_KEY: str = os.getenv('SECRET_KEY')

# Подключение к БД
DB_USER: str = os.getenv("DB_USER")
DB_PASSWORD: str = os.getenv("DB_PASSWORD")
DB_NAME: str = os.getenv("DB_NAME")
DB_HOST: str = 'localhost' if DEBUG else os.getenv("DB_HOST")
DB_PORT: int = os.getenv("DB_PORT")
DB_URL: str = (
    "postgresql+asyncpg://"
    + f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Подключение к БД (Для тестирования!)
DB_USER_TEST: str = os.getenv("DB_USER_TEST")
DB_PASSWORD_TEST: str = os.getenv("DB_PASSWORD_TEST")
DB_NAME_TEST: str = os.getenv("DB_NAME_TEST")
DB_HOST_TEST: str = 'localhost' if DEBUG else os.getenv("DB_HOST_TEST")
DB_PORT_TEST: int = os.getenv("DB_PORT_TEST")
DB_URL_TEST: str = (
    "postgresql+asyncpg://"
    + f"{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}"
    + f"/{DB_NAME_TEST}"
)

# Домен сервера Яндекс Маркета
YM_DOMAIN: str = 'http://localhost:8001'

# Домен сервера DS
DS_DOMAIN: str = 'http://localhost:8002'

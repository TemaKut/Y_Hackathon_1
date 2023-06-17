from loguru import logger

from app.settings import BASE_DIR


logger.remove()
logger.add(
    f"{BASE_DIR}/logs/logs.log",
    level='DEBUG',
    rotation="2 MB",
    format=(
        "{time:YYYY-MM-DD at HH:mm:ss} "
        "| {level} | {name} {line} | {message}"
    ),
)

# Всё логгирование только через этот объект!
log = logger

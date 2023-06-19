# Проект хакатона от Yandex Market. Команда № 1

Состав команды:
- Project Manager: @nik_gorbunova
- Designer: @teufelitto @khod_ss
- Frontend developer: @lipnickaite @KanapinM
- Backend developer: @TemaCu @voyager1744
- DS: @Rumia_s @SciManNik @IrinaBalycheva


Рабочие директории/файлы и ответственные за них разработчики:
- backend/ -> @TemaCu
- yandex_mock_server/ -> @TemaCu
- frontend/ -> @lipnickaite @KanapinM
- ds/ -> @Rumia_s @SciManNik @IrinaBalycheva
- docker-compose.yml -> @TemaCu


# Кратко о работе DS и разработчиков

backend:
- Язык Python
- Написан на библиотеке FastAPI
- Написан моковый сервер так же на FastAPI (Для симуляции реальной коммуникации между backend и сервером Yandex Market)
- Код написан в асинхронной стилистике с соблюдением PEP8, а так же типизацией.
- Реализовал взаимодействие с пользователями при помощи БД PostgreSQL и ORM SQLAlchemy
- Написаны соответствующие тесты при помощи pytest

frontend:
- Язык JavaScript
- Написан на библиотеке React
- Реализована статика приложения в соответствии с дизайном
- Рализовано взаимодействие с api в асинхронной стилистике с применением axios

ds:
- Выполнена предобработка исходных данных
- Проведен исследовательский анализ данных
- Сгенерированы новые признаки для обучения модели на основании выявленных зависимостей
- Для предсказания разработана модель LGBMClassifier, подобраны оптимальные гиперпараметры
- Проведено тестирование, в результате которого получены метрики F1_macro и Accuracy
- Создан API сервер на FastAPI для взаимодействия по REST API


# Запуск проекта локально (По порядку)

- Переходим в корневую директорию проекта (Y_Hackathon_1/)
- В файле docker-compose.yml указать .env переменные (Изначально - подставлены переменные по умолчанию с целью упрощённого запуска. На боевом сервере убрать в Git secrets)
- Запустить демон Docker
- Находясь в терминале в директории (Y_Hackathon_1/) выполнить команду "docker-compose up -d"

# После успешного запуска будут заняты соответствующие порты на localhost
- http://localhost:8000/docs (Документация backend)
- http://localhost:8001/docs (Документация yandex mock server)
- http://localhost:8002/docs (Документация сервера DS)
- http://localhost:3000/ (Полноценное приложение (frontend))

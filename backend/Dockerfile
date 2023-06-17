FROM python:3.11-slim

WORKDIR /backend

COPY ./app /backend/app
COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

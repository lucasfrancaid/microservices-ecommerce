FROM python:3.9-slim-buster

WORKDIR /app

ADD ./Pipfile ./Pipfile.lock ./
RUN pip install pipenv && pipenv install --system

ADD . .
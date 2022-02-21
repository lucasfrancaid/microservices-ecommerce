FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update -y && apt upgrade -y && apt install -y make

ADD ./Pipfile ./Pipfile.lock ./
RUN pip install -U pip && pip install pipenv && pipenv install --system

ADD . .
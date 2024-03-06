# syntax=docker/dockerfile:1.4

FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

RUN ["chmod", "+x", "/app/entrypoint.sh"]

ENTRYPOINT /app/entrypoint.sh


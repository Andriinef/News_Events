FROM python:3.10-alpine
# MAINTAINER Andrii Nefodov

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /news
WORKDIR /news
COPY ./news /news

RUN adduser -D user

USER user

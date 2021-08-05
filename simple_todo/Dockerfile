FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/simple_todo/
RUN mkdir -p /usr/src/static/
WORKDIR /usr/src/simple_todo/

COPY simple_todo/requirements.txt .

RUN pip install -r requirements.txt
COPY simple_todo/ .

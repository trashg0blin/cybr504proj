FROM python:3.8.3-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt /code/

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev curl cargo musl-dev openssl-dev
#need rust to build cryptography package
RUN export CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ /code/

RUN python /code/manage.py migrate
FROM python:3.9.0-alpine

LABEL maintainer="i.ishbaev@innopolis.unviversity"

RUN adduser --disabled-password app -s /bin/sh -h /home/app

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip --no-cache-dir install -U pip && pip3 install --no-cache-dir --ignore-installed -r requirements.txt

COPY app_python /app

USER app

ENV DEBUG=True 
EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]

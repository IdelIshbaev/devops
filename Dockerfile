FROM python:3.9.0-alpine

WORKDIR /app

RUN apk update

COPY requirements.txt /app/
RUN python -m pip --no-cache-dir install -U pip && pip3 install --no-cache-dir --ignore-installed -r requirements.txt

COPY app_python /app

ENV DEBUG=True 
EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]

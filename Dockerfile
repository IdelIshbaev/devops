FROM python:3.9.0-alpine

LABEL maintainer="i.ishbaev@innopolis.unviversity"

WORKDIR /app

RUN adduser --disabled-password app && chown -R app /app

USER app

COPY requirements.txt /app/
RUN python -m pip --no-cache-dir install -U pip && pip3 install --no-cache-dir --ignore-installed -r requirements.txt

COPY app_python /app

ENV FLASK_APP=app
ENV FLASK_ENV=development

#ENV DEBUG=True
EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0"]

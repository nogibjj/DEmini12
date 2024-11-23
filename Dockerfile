# FROM alpine:latest
# RUN apk update && apk add bash
# WORKDIR /app
# COPY repeat.sh /app

FROM python:3.9-slim

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app

EXPOSE 5000

CMD ["python", "main.py","mlflow", "server","--host",  "sqlite:///mlflow.db",  "/app/mlruns", "--host", "0.0.0.0", "5000","--port"]


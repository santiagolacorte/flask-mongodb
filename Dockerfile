# Base image
FROM python:3.10-slim AS prod

ENV APP_HOME /app
ENV PYTHONUNBUFFERED True

WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN pip install --no-cache-dir -r requirements.txt


# Development image
FROM prod AS dev

RUN pip install --no-cache-dir -r requirements-dev.txt

CMD gunicorn --bind :${APP_PORT} --workers 1 --threads 8 --timeout 0 src.app:app

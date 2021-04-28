FROM python:3.8-slim as core
RUN pip install pipenv==2020.11.15

WORKDIR  /app

COPY Pipfile /app
COPY Pipfile.lock /app
RUN pipenv install --system

FROM core as dev

RUN pipenv install --system --dev

COPY . /app

CMD ["sh", "./scripts/validate.sh"]

FROM core as web
ENV HOST="0.0.0.0"
ENV PORT="8001"
ENV PYTHONPATH="/app"


COPY ./isseven /app/isseven
COPY ./static_assets /app/static_assets
COPY ./templates /app/templates
COPY ./README.md /app

CMD ["sh", "-c", "gunicorn isseven:app -w 1 -k uvicorn.workers.UvicornWorker -b ${HOST}:${PORT}"]
FROM python:3.9.18-alpine3.18 as base

RUN pip install "poetry==1.3.2"

COPY ./poetry.lock .
COPY pyproject.toml .

RUN poetry install
COPY ./todo_app ./todo_app

FROM base as production
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
EXPOSE 8000 

FROM base as development
ENTRYPOINT poetry run flask run --host 0.0.0.0 --port 8000
EXPOSE 8000 
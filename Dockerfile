FROM python:3.9.18-alpine3.18

RUN pip install "poetry==1.3.2"

COPY ./todo_app ./todo_app
COPY ./poetry.lock .
COPY pyproject.toml .

RUN poetry install

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

EXPOSE 8000 
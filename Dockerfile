FROM python:3.9.16-bullseye
ENV POETRY_VERSION=1.3.2

RUN apt-get update -y
RUN apt-get install curl -y
RUN apt install gunicorn3 -y

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

WORKDIR /app

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$ENVIRONMENT" == PROD && echo "--no-dev") --no-interaction --no-ansi

COPY ./ /app/

EXPOSE ${PORT}


CMD ["/bin/bash", "./scripts/entrypoint.sh"]

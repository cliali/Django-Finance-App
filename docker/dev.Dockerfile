# This docker file is used for local development via docker-compose
# Creating image based on official python3 image
FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Required to install mysqlclient with Pip
RUN apt-get update \
  && apt-get install python3-dev efault-libmysqlclient-dev gcc -y

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-cache

# Fix python printing
ENV PYTHONUNBUFFERED 1

# Get the django project into the docker container
COPY . /app

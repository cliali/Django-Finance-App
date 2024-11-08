default:
  just --list

run *args:
  uv run manage.py runserver {{args}}

migrate:
  uv run manage.py migrate

makemigrations:
  uv run manage.py makemigrations

createsuperuser *args:
  uv run manage.py createsuperuser {{args}}

ruff *args:
  uv run ruff check {{args}} finance_config

lint:
  uv run ruff format finance_config
  just ruff --fix

# docker
up:
  docker compose up -d

dev-up:
  docker compose -f docker-compose.dev.yml up -d

down:
  docker compose down

dev-down:
  docker compose -f docker-compose.dev.yml down

kill *args:
  docker compose kill {{args}}

build:
  docker compose build

dev-build:
  docker compose -f docker-compose.dev.yml build

ps:
  docker compose ps
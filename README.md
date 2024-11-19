# Django-Finance-App

## project setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd Django-Finance-App
```

2- SetUp venv (install uv first)
```
uv venv
source .venv/bin/activate
```

3- install Dependencies
```
uv pip install -r pyproject.toml
```

4- create your env
```
cp .env.example .env
```

5- Create tables
```
python manage.py migrate
```
or (with just)
```
just migrate
```

6- spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```
or
```
just dev-up
```

7- run the project
```
python manage.py runserver
```
or
```
just run
```
# Authentication Service

## Responsibilities
- Sign Up
- Sign In
- Recovery Password

## Stack
- **Software Design**: Clean Architecture
- **Language**: Python 3.9
- **DBMS**: PostgreSQL
- **API Rest Framework**: FastAPI (Async)
- **ORM Framework**: SqlAlchemy (Async) + Alembic (for Migrations)
- **Test Framework**: Pytest (Async)

## Setup
Install packages and activate virtual environment:
```bash
pipenv install
pipenv shell
```

Run postgres database with Docker Compose:
```bash
docker-compose up -d postgres
make migrate
```

Run application:
```bash
make run
```

Run application with Docker Compose (*Don't need packages installation, database initialization and migrate command*):
```bash
docker-compose up --build postgres server
```

- Health Check: http://127.0.0.1:8000/health-check
- Swagger: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## Tests
To run tests locally, is necessary activate virtualenv:
```bash
pipenv shell
```

Running all tests (Slower):
```bash
make test args='-v'
```

Running core tests (Faster):
```bash
make test args='-v -m "not fastapi and not sqlalchemy"'
```

Running adapter tests (Faster):
```bash
make test args='-v -m fastapi' # or sqlalchemy
```

Coverage generate:
```bash
make coverage # Current coverage: 99%
```

## Migrations
To run migrations, is necessary activate virtualenv:
```bash
pipenv shell
```

Making a new migration:
```bash
make migration message='Add Users table' # Change message according to implementation
```
Upgrading database with migrations:
```bash
make migrate
```

## To do
- Sign In Use Case
- Recovery Password Use Case
- Add a free email service
- Test src.infrastructure.orm.migrations
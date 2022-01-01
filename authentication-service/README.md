# Authentication Service

## Responsibilities
- Sign Up
- Sign In
- Recovery Password

## Stack
- **Language**: Python 3.9
- **DBMS**: PostgreSQL 12
- **API Rest Framework**: FastAPI (Async)
- **ORM Framework**: SqlAlchemy (Async)
- **Test Framework**: Pytest (Async)

## Setup
Install packages and activate virtual environment:
```bash
pipenv install
pipenv shell
```

Run application:
```bash
make run
```

Run application with Docker Compose:
```bash
docker-compose up --build
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
make test args='-v -s'
```

Running core tests (Faster):
```bash
make test args='-v -s -m "not fastapi and not sqlalchemy"'
```

Running adapter tests (Faster):
```bash
make test args='-v -s -m fastapi' # or sqlalchemy
```

Coverage generate:
```bash
make coverage
```

## To do
- Add Alembic to manage migrations (Improve database startup)
- Add a free email service
- Sign In Use Case
- Recovery Password Use Case
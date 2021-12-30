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

Create a .env file:
```bash
cp .env.sample .env
```

Run application:
```bash
make run
```

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
make test args='-v -s -m "not fastapi and not sqlite"'
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
- Test infrastructure.orm and adapters.http.fastapi.main
- Implement delete method in Sqlite Repository
- Add a free email service
- Add PostgreSQL as Database with SqlAlchemy (add database strategy to instance from env config)
- Sign In Use Case
- Recovery Password Use Case
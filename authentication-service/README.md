# Authentication Service

## Responsibilities
- Sign Up
- Sign In
- Recovery Password

## Stack
- Python 3.9
- SqlAlchemy Async
- PostgreSQL
- Pytest
- FastAPI as Adapter

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
make test args='-v -s -m fastapi' # or sqlite
```


Coverage generate:
```bash
make coverage
```

## To do
- Add a free email service
- Add PostgreSQL as Database with SqlAlchemy (add databse strategy to instance from env config)
- Sign In Use Case
- Recovery Password Use Case
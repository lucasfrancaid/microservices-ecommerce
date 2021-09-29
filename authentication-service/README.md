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

## Tests
To run tests locally, is necessary activate virtualenv:
```bash
pipenv shell
```

Running tests:
```bash
make test args=-v
```

Coverage generate:
```bash
make coverage
```
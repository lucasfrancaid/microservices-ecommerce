# Catalog Service
This is a Service for management the products

## Responsibilities
- Manage Products
- Manage Categories

## Stack
- **Software Design**: Clean Architecture / Hexagonal
- **Language**: Python 3.9
- **NoSQL DB**: MongoDB
- **API Rest Framework**: FastAPI (Async)
- **ORM Framework**: ODMantic (Async)
- **Test Framework**: Pytest (Async)

## Setup
Add .env file:
```bash
cp .env.sample .env
```

Install packages and activate virtual environment:
```bash
pipenv install
pipenv shell
```

Run mongo database with Docker Compose:
```bash
docker-compose up -d mongo
```

Run application:
```bash
make run
```

Run application with Docker Compose (*Don't need packages installation, database initialization and migrate command*):
```bash
docker-compose up --build mongo server
```

- Health Check: http://127.0.0.1:8000/health-check
- Swagger: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## Tests
To run tests locally, is necessary activate virtualenv:
```bash
pipenv install --dev
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

## To do
- ?

## API Contract
 /catalog
```json
{
    "promotions": {
        "maxDiscount": 70,
        "productsCount": 1500,
        "products": [
            {

            }
        ]
    },
    "recommended": {
        "productsCount": 100,
        "products": {

        }
    }
}
```

/catalog/{productId}

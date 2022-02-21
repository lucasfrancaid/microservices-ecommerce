ENV_FILE := .env
PYTHON_PATH := $(shell pwd)

run:
	@echo '--> Starting Catalog Service'
	@PYTHONPATH=${PYTHON_PATH} python ./src/main.py

test:
	@echo '--> Running Tests for Authentication Service'
	@pytest $(args)

coverage:
	@coverage run --source src -m pytest
	@coverage report -m
	@coverage html

run_docker:
	@echo '--> Starting Catalog Service with Docker'
	@docker-compose up

pre-commit:
	@echo '--> Running pre-commit yapf formatter and pytest hooks'
	@pre-commit install
	@pre-commit run --all-files

clean_cache:
	@echo "--> Cleaning python cache"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@echo "--> Ok"

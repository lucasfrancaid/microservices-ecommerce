ENV_FILE := .env
PYTHON_PATH := $(shell pwd)

run:
	@echo '--> Starting Authentication Service'
	@PYTHONPATH=${PYTHON_PATH} python ./src/adapters/http/fastapi/main.py

test: dev_packages
	@echo '--> Running Tests for Authentication Service'
	@python -m pytest $(args)

coverage:
	@coverage run --source src -m pytest
	@coverage report -m
	@coverage html

pre-commit:
	@echo '--> Running pre-commit yapf formatter and pytest hooks'
	@pre-commit install
	@pre-commit run --all-files

dev_packages:
	@echo '--> Installing dev packages'
	@pipenv install --dev

clean_cache:
	@echo "--> Cleaning python cache"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@echo "--> Ok"

ENV_FILE := .env

run:
	@echo '--> Starting Authentication Service'
	@uvicorn service.adapters.fastapi.main:app --host 0.0.0.0 --port 8000

test: dev_packages
	@echo '--> Running Tests for Authentication Service'
	@python -m pytest $(args)

coverage:
	@coverage run --source service -m pytest
	@coverage report -m
	@coverage html

dev_packages:
	@echo '--> Installing dev packages'
	@pipenv install --dev

clean_cache:
	@echo "--> Cleaning python cache"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@echo "- Ok"

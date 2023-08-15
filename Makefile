ENV=development
PROJECT=proj3ct

TEST_FILES=./tests

FLAKE8_FLAGS = --ignore=W503,E501
ISORT_FLAGS = --profile=black --lines-after-import=2


.PHONY: all help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## @ Environment
.PHONY: clean install

install: ## Install dependencies to run project in development environment
	pip install -U pip setuptools wheel pip-tools pre-commit
	pip install -r requirements-dev.txt
	pip install -r requirements.in
	pip-compile --output-file=requirements.txt requirements.in
	pre-commit install

clean: ## Remove cache files from project
	@echo "cleaning cache files"
	@py3clean .
	@rm -rf .cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov coverage-report coverage .coverage
	@rm -rf .tox/
	@rm -rf docs/_build
	@rm -rf docs/_build
	@echo "Done!"

## @ Application - See pyproject.toml
.PHONY: test run
test: ## Run tests and save coverage
	@pytest

run: ## Run application by django server
	@python manage.py runserver --insecure

migrate: ## Run migrations
	@python manage.py migrate

makemigrations: ## Make migrations
	@python manage.py makemigrations

shell: ## Run django shell
	@python manage.py shell_plus --ipython -- --profile=recipes

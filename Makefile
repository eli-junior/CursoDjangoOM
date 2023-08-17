ENV=development
PROJECT=proj3ct

TEST_FOLDER=./tests

FLAKE8_FLAGS = --ignore=
ISORT_FLAGS = --profile=django --lines-after-import=2


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


.PHONY: test run admin populate migrate migrations shell ## @ Application - See pyproject.toml
test: ## Run tests and save coverage
	@pytest

run: ## Run application by django server
	@python manage.py runserver --insecure

admin: ## Create admin user
	@python manage.py createsuperuser --username admin --email admin@localhost

populate: ## Populate database with fake data
	@echo "Recriando banco de dados"
	@rm -f db.sqlite3
	@make migrate
	@echo "Criando novo usuário admin. Digite a senha abaixo:"
	@make admin
	@echo "Populando banco de dados com dados falsos"
	@python manage.py populate_recipes -f

migrate: ## Run migrations
	@python manage.py migrate

migrations: ## Run make migrations
	@python manage.py makemigrations

shell: ## Run django shell
	@python manage.py shell_plus --ipython -- --profile=recipes


.PHONY: lint format ## @ Linters
lint: ## Run ruff and isort as linters
	@ruff check $(PROJECT) $(TEST_FOLDER)
	@isort --check $(ISORT_FLAGS) $(PROJECT) $(TEST_FOLDER)

format:
	@isort $(ISORT_FLAGS) $(PROJECT) $(TEST_FOLDER)
	@ruff $(PROJECT) $(TEST_FOLDER)

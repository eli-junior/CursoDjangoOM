install:
	pip install -r requirements-dev.txt
	pip install -r requirements.in
	pip-compile --output-file=requirements.txt requirements.in
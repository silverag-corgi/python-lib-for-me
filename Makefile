help:
	@echo set target to run "make" command
	@echo target: lint, format

lint:
	@echo -------------------- check grammar --------------------
	poetry run pflake8 .
	@echo -------------------- check import statement --------------------
	poetry run isort --check --diff .
	@echo -------------------- check type --------------------
	poetry run mypy .

format:
	@echo -------------------- format import statement --------------------
	poetry run isort .

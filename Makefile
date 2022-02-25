help:
	@echo set target to run "make" command
	@echo target: lint, format, test

lint:
	@echo -------------------- run pflake8 to check grammar ----------------------------------------
	@poetry run pflake8 .
	@echo -------------------- run isort to check import statement ---------------------------------
	@poetry run isort --check --diff .
	@echo -------------------- run mypy to check type ----------------------------------------------
	@poetry run mypy .

format:
	@echo -------------------- run isort to format import statement --------------------------------
	@poetry run isort .

test:
	@echo -------------------- run pytest to test --------------------------------------------------
	@poetry run pytest --verbose

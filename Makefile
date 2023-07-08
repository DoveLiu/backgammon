lint:
	poetry run black . 
	poetry run ruff . --fix
.PHONY: lint

run:
	poetry run python main.py
.PHONY: run

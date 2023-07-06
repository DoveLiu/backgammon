lint:
	poetry run black . 
	poetry run ruff . --fix
.PHONY: lint

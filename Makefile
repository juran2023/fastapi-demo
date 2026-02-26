fmt:
	ruff check . --fix
	black .

test:
	pytest -q

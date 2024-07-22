PYTHON := .venv/bin/python

install:
	python3 -m venv .venv
	$(PYTHON) -m pip install -e .[dev]

qa:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m mypy .
	$(PYTHON) -m pytest .

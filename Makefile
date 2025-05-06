install:
	pip install -e .

test:
	pytest

lint:
	flake8 fastapi_debug_toolkit

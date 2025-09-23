PYTHON=python
PIP=pip

.PHONY: install api cli

install:
	$(PIP) install -r requirements.txt

api:
	uvicorn api.server:app --host 0.0.0.0 --port 8000

cli:
	$(PYTHON) -m app.cli.main "$(TOPIC)"

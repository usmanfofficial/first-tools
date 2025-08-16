.PHONY: venv install test run
venv:
	python3 -m venv .venv
install:
	. .venv/bin/activate && pip install -r requirements.txt
test:
	. .venv/bin/activate && pytest -q
run:
	python hello.py

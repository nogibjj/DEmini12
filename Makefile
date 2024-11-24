SHELL := /bin/bash

VENV_PATH := $(PWD)/venv
PYTHON := $(VENV_PATH)/bin/python

install:
	python3 -m venv $(VENV_PATH) && \
	$(PYTHON) -m pip install --upgrade pip && \
	$(PYTHON) -m pip install --no-cache-dir -r requirements.txt

test:
	$(PYTHON) -m pytest test_*.py

format:	
	$(PYTHON) -m black *.py 

lint:
	$(PYTHON) -m pylint --disable=E,F,C,W *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# deploy steps go here
		
all: install lint test format deploy

generate_and_push:
	$(PYTHON) test_main.py

ml_run:
	$(PYTHON) -m pip install mlflow && \
	MLFLOW_TRACKING_URI="file:./mlruns" $(PYTHON) main.py
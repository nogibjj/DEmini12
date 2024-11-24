install:
	pip install --upgrade pip &&\
		pip install --no-cache-dir -r requirements.txt

test:
	python -m pytest test_*.py

format:	
	black *.py 

lint:
	pylint --disable=E,F,C,W *.py


container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

generate_and_push:
	# Create the markdown file 
	python test_main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "Sammyissmiling@gmail.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

ml_run:
	MLFLOW_TRACKING_URI=file:./mlruns python main.py
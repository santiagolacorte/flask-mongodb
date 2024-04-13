.PHONY: venv
venv: # Create a virtual environment
	@echo "=============================="
	@echo "Creating a virtual environment..."
	@echo "=============================="
	@rm -rf .venv
	@python3 -m venv .venv
	@echo
	@echo "Run 'source .venv/bin/activate' to enable the environment"


.PHONY: install
install: # Install dependencies
	@echo "=============================="
	@echo "Installing dependencies..."
	@echo "=============================="
	@echo
	pip install -r requirements-dev.txt
	pip install -r requirements-test.txt
	pip install -r requirements.txt


.PHONY: fmt
fmt: # Formatting Python code
	isort src/
	isort tests/
	autopep8 --experimental --max-line-length 100 --in-place --recursive src/
	autopep8 --experimental --max-line-length 100 --in-place --recursive tests/


.PHONY: lint
lint: # Check code smells with Ruff
	@echo "=============================="
	@echo "Searching for code smells..."
	@echo "=============================="
	@echo
	@mkdir -p reports/lints-reports || true
	@ruff check --exit-zero --output-format json -o reports/lint-report-ruff.json .
	@ruff check --exit-zero --output-format text .


.PHONY: clean
clean: # Clean unused filed
	@find . -name '*_cache*' -exec rm -rf {} +
	@find . -name '*__*cache__*' -exec rm -rf {} +
	@rm -rf reports/ || true
	@rm -rf .coverage || true
	@rm -rf htmlcov


.PHONY: tests
tests: # Run tests and coverage with Pytest
	@echo "=============================="
	@echo "Running unit tests..."
	@echo "=============================="
	@pytest

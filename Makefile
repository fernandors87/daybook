MAIN_FILE=daybook/main.py

.PHONY: run
run:
	- python $(MAIN_FILE)

.PHONY: test
test:
	- python -m pytest --cov=daybook --cov-fail-under=85

.PHONY: type-checking
type-checking:
	- mypy $(MAIN_FILE) --strict
	- mypy nubank_checking_account.py --strict
	- mypy nubank_credit_card.py --strict

.PHONY: lint
lint:
	- flake8

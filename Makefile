.PHONY: type-checking
lint:
	- flake8

.PHONY: type-cheking
type-checking:
	- mypy main.py --strict
	- mypy nubank_checking_account.py --strict
	- mypy nubank_credit_card.py --strict
from pprint import pprint
from typing import Any, cast

import yaml

from models.v1 import Book, ParsedBook


def open_book() -> dict[str, Any]:
    with open('ledger.yml') as file:
        yml: Any = yaml.load(file, Loader=yaml.FullLoader)
        return cast(dict[str, Any], yml)


def balance(book: Book) -> dict[str, float]:
    report: dict[str, float] = {}
    for transaction in book.transactions:
        for r in transaction.records:
            report[r.account] = report.get(r.account, 0) + r.value
    return report


def normalize_book(book: ParsedBook) -> Book:
    updated_book = Book(
        name=book.name,
        transactions=[tx.detailed() for tx in book.transactions]
    )
    return updated_book


if __name__ == '__main__':
    raw_book = open_book()
    parsed_book = ParsedBook(**raw_book)
    normalized_book = normalize_book(parsed_book)
    balance_report = balance(normalized_book)
    pprint(balance_report)

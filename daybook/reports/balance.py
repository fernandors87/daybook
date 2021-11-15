import pprint
from typing import Any, Dict

from models.v1 import Book


class BalanceReport():
    book: Book
    data: Dict[str, Any]

    def __init__(self, book: Book):
        self.book = book
        self.data = {}
        self._process_data()

    def __str__(self) -> str:
        return pprint.pformat(self.data)

    def _process_data(self) -> None:
        self.data = {}

        for transaction in self.book.transactions:
            for r in transaction.records:
                self.data[r.account] = self.data.get(r.account, 0) + r.value

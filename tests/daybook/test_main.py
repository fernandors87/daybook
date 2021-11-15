from datetime import date

from daybook import main
from daybook.models.v1 import ParsedBook, Record, ShortTransaction, Transaction


def test_normalize_book():
    records = [Record(account='acc3', value=23.4), Record(account='acc4', value=-23.4)]
    transactions = [
        ShortTransaction(date=date(2021, 1, 1), accounts=['acc1', 'acc2'], value=12.3),
        Transaction(date=date(2021, 1, 2), records=records)
    ]
    book = ParsedBook(
        version='1.0',
        transactions=transactions
    )
    normalized = main.normalize_book(book)
    assert normalized.transactions == [
        Transaction(date=date(2021, 1, 1), records=[
            Record(account='acc1', value=12.3), Record(account='acc2', value=-12.3)
        ]),
        Transaction(date=date(2021, 1, 2), records=[
            Record(account='acc3', value=23.4), Record(account='acc4', value=-23.4)
        ])
    ]

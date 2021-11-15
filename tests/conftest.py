from datetime import date

import pytest

from daybook.models.v1 import (Book, ParsedBook, Record, ShortTransaction,
                               Transaction)


@pytest.fixture
def book_john_raw():
    records = [Record(account='acc3', value=23.4), Record(account='acc4', value=-23.4)]
    transactions = [
        ShortTransaction(date=date(2021, 1, 1), accounts=['acc1', 'acc2'], value=12.3),
        Transaction(date=date(2021, 1, 2), records=records)
    ]
    return ParsedBook(
        version='1.0',
        name='John\'s Book',
        transactions=transactions
    )


@pytest.fixture
def book_john():
    transactions = [
        Transaction(
            date=date(2021, 1, 1),
            records=[
                Record(account='acc1', value=12.3),
                Record(account='acc2', value=-12.3)
            ]
        ),
        Transaction(
            date=date(2021, 1, 2),
            records=[
                Record(account='acc3', value=23.4),
                Record(account='acc4', value=-23.4)
            ]
        )
    ]
    return Book(
        name='John\'s Book',
        transactions=transactions
    )

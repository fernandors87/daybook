from daybook.reports.balance import BalanceReport
from models.v1 import Book


def test_balance_report_data(book_john: Book) -> None:
    report = BalanceReport(book_john)
    assert report.data == {
        'acc1': 12.3,
        'acc2': -12.3,
        'acc3': 23.4,
        'acc4': -23.4
    }


def test_balance_report_data_when_book_is_empty(book_empty: Book) -> None:
    report = BalanceReport(book_empty)
    assert report.data == {}


def test_balance_report_str(book_john: Book) -> None:
    report = BalanceReport(book_john)
    assert str(report) == "{'acc1': 12.3, 'acc2': -12.3, 'acc3': 23.4, 'acc4': -23.4}"

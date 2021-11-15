from daybook import main


def test_normalize_book(book_john_raw, book_john):
    normalized = main.normalize_book(book_john_raw)
    assert normalized == book_john


def test_balance(book_john):
    report = main.balance(book_john)
    assert report == {
        'acc1': 12.3,
        'acc2': -12.3,
        'acc3': 23.4,
        'acc4': -23.4
    }

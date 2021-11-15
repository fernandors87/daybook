from daybook import main


def test_normalize_book(book_john_raw, book_john):
    normalized = main.normalize_book(book_john_raw)
    assert normalized == book_john

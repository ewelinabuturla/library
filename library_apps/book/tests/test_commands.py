from unittest.mock import call, patch

import pytest
from django.core.management import call_command

from ..models import Book


@pytest.mark.django_db
def test_populate_books():
    with patch("logging.info") as mocked_logging:
        call_command("populate_books", filename="books.csv")
        books = Book.objects.all()
        expected_calls = [call(f"Book ISBN: {book.isbn} added.") for book in books]
        mocked_logging.assert_has_calls(expected_calls, any_order=True)

    assert books


@pytest.mark.django_db
def test_populate_books_file_not_found():
    with patch("logging.error") as mocked_logging:
        call_command("populate_books", filename="test.csv")
        mocked_logging.assert_called_with("File does not exist.")

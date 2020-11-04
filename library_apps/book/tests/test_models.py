import pytest

from .factories import BookFactory


@pytest.mark.django_db
def test_book_str():
    book = BookFactory()
    assert book.__str__() == f"Book {book.title} - author {book.author.name}"

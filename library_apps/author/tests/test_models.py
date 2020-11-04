import pytest

from .factories import AuthorFactory


@pytest.mark.django_db
def test_author_str():
    author = AuthorFactory()
    assert author.__str__() == f"Author {author.name}"

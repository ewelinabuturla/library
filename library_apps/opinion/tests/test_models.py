import pytest

from .factories import OpinionFactory


@pytest.mark.django_db
def test_opinion_str():
    opinion = OpinionFactory()
    assert (
        opinion.__str__() == f"Rating: {opinion.rating} for book {opinion.book.title}"
    )

from unittest.mock import call, patch

import pytest
from django.core.management import call_command

from ..models import Opinion


@pytest.mark.django_db
def test_populate_opinions():
    with patch("logging.info") as mocked_logging:
        # First upload books
        call_command("populate_books", filename="books.csv")
        call_command("populate_opinions", filename="opinions.csv")
        opinions = Opinion.objects.all()
        expected_calls = [call(f"Opinion: {opinion.id} added.") for opinion in opinions]
        mocked_logging.assert_has_calls(expected_calls, any_order=True)

    assert opinions


@pytest.mark.django_db
def test_populate_opinions_file_not_found():
    with patch("logging.error") as mocked_logging:
        call_command("populate_opinions", filename="test.csv")
        mocked_logging.assert_called_with("File does not exist.")

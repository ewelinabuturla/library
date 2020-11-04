import pytest
from django.urls import reverse

from .factories import BookFactory


@pytest.mark.django_db
def test_book_list_view_success(api_client):
    [BookFactory() for _ in range(5)]
    response = api_client.get(reverse("book:list"))

    assert response.status_code == 200
    assert response.json()["count"] == 5


@pytest.mark.django_db
def test_book_detail_view_success(api_client):
    book = BookFactory()
    response = api_client.get(reverse("book:detail", args=[book.title]))

    assert response.status_code == 200
    assert response.json()["title"] == book.title

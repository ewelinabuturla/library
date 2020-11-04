import factory
import factory.fuzzy

from ...author.tests.factories import AuthorFactory
from ..models import Book


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=255)
    isbn = factory.fuzzy.FuzzyText(length=13)
    genre = factory.fuzzy.FuzzyText(length=50)
    author = factory.SubFactory(AuthorFactory)

    class Meta:
        model = Book

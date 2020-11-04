import factory
import factory.fuzzy

from ...book.tests.factories import BookFactory
from ..models import Opinion


class OpinionFactory(factory.django.DjangoModelFactory):
    description = factory.fuzzy.FuzzyText(length=255)
    rating = factory.fuzzy.FuzzyInteger(1, 5)
    book = factory.SubFactory(BookFactory)

    class Meta:
        model = Opinion

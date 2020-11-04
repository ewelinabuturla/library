import factory
import factory.fuzzy

from ..models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=50)

    class Meta:
        model = Author

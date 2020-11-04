from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ..book.models import Book


class Opinion(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="opinions")

    def __str__(self):
        return f"Rating: {self.rating} for book {self.book.title}"

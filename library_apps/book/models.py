from django.db import models

from ..author.models import Author


class Book(models.Model):
    GENRE_CHOICES = [
        ("Kryminał", "Kryminał"),
        ("Literatura młodzieżowa", "Literatura młodzieżowa"),
        ("Literatura obyczajowa", "Literatura obyczajowa"),
        ("Romans", "Romans"),
        ("Fantastyka", "Fantastyka"),
        ("Sensacja", "Sensacja"),
        ("Literatura faktu", "Literatura faktu"),
    ]

    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")

    def __str__(self):
        return f"Book {self.title} - author {self.author.name}"

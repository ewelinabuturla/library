import csv
import logging
import os

from django.core.management.base import BaseCommand

from ....author.models import Author
from ...models import Book


class Command(BaseCommand):
    help = "Populate books from csv file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--filename",
            help="CSV file path to populate Books.",
            type=str,
            required=True,
        )

    def handle(self, *args, **options):
        if os.path.isfile(options["filename"]):
            with open(options["filename"], mode="r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                # Consume header
                next(csv_reader)
                for row in csv_reader:
                    author, _ = Author.objects.update_or_create(name=row[2])
                    book, _ = Book.objects.update_or_create(
                        isbn=row[0],
                        author=author,
                        defaults={"title": row[1], "genre": row[3]},
                    )
                    logging.info(f"Book ISBN: {book.isbn} added.")
        else:
            logging.error("File does not exist.")

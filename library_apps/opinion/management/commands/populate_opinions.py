import csv
import logging
import os

from django.core.management.base import BaseCommand

from ....book.models import Book
from ...models import Opinion


class Command(BaseCommand):
    help = "Populate opinions for books from csv file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--filename",
            help="CSV file path to populate Opinions.",
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
                    book = Book.objects.get(isbn=row[0])
                    opinion, _ = Opinion.objects.update_or_create(
                        book=book, rating=row[1], description=row[2],
                    )
                    logging.info(f"Opinion: {opinion.id} added.")
        else:
            logging.error("File does not exist.")

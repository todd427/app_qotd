# qotd/management/commands/import_quotes.py

import json
from django.core.management.base import BaseCommand
from qotd.models import Quote

class Command(BaseCommand):
    help = "Import quotes from a JSON file into the database"

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r', encoding='utf-8') as f:
            quotes = json.load(f)

        count = 0
        for entry in quotes:
            Quote.objects.create(
                text = entry['quote'],
                author = entry['author'],
                url = entry.get('url', ''),
                source = entry.get('source', '')
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {count} quotes from {json_file}'))

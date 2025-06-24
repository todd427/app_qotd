# qotd/management/commands/unapprove_all_quotes.py

from django.core.management.base import BaseCommand
from qotd.models import Quote

class Command(BaseCommand):
    help = "Unapprove all quotes in the database"

    def handle(self, *args, **kwargs):
        updated = Quote.objects.filter(approved=True).update(approved=False)
        self.stdout.write(self.style.SUCCESS(f"Unapproved {updated} quotes!"))

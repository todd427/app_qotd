# qotd/management/commands/approve_all_quotes.py

from django.core.management.base import BaseCommand
from qotd.models import Quote

class Command(BaseCommand):
    help = "Approve all quotes in the database"

    def handle(self, *args, **kwargs):
        updated = Quote.objects.filter(approved=False).update(approved=True)
        self.stdout.write(self.style.SUCCESS(f"Approved {updated} quotes!"))

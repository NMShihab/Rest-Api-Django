import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command execution until db available"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for db..')
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections['default']
            except OperationalError:
                self.stdout.write("Db unavailable, waiting 1 second...")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("Db available"))
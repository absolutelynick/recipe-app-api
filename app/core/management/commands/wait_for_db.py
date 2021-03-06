import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Pause execution until the database is available. """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        seconds = 1
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(f'Database unavailable, '
                                  f'waiting for {seconds} seconds...')
                time.sleep(seconds)
                seconds += seconds

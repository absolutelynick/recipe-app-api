from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """ Test waiting for db when db is available. """

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')

            # Checking that the db item was called and returned once
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test waiting for db. Replaces the function of time.sleep. """

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:

            # Side effect will raise the operation error
            # 5 times and let it pass on the sixth
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')

            # Asserting that we have reached the count of 6
            self.assertEqual(gi.call_count, 6)

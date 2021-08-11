from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # Here we creating mock,
        # everytime we calling connectionHandler.getItem
        # we will call that mock instead
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # This way is to create mock for time.sleep, in order it to work,
    # we also need to pass the argument as a parameter to the function
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        #  [OperationalError] * 5 + [True] -
        #  means that we expecting it to throw OperationalError first 5 times,
        #  and at the sixth time it return succeed.
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

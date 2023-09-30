import hw_14_test
import unittest

class TestAccount(unittest.TestCase):
    def test_create_account(self):
        new_account = Account.create_account('NEW789')
        self.assertEqual(new_account.get_balance(), 0.0)
        self.assertEqual(new_account.get_account_number(), 'NEW789')
import hw_14_test
from unittest.mock import patch, MagicMock
import unittest

class TestAccount(unittest.TestCase):
    def test_create_account(self):
        new_account = Account.create_account('NEW789')
        self.assertEqual(new_account.get_balance(), 0.0)
        self.assertEqual(new_account.get_account_number(), 'NEW789')

    def test_update_accounts(self):
            savings_account = hw_14_test.SavingsAccount(1000.0, 'SAV123', 5.0)
            current_account = hw_14_test.CurrentAccount(500.0, 'CUR456', 100.0)

            bank = hw_14_test.Bank()
            bank.add_account(savings_account)
            bank.add_account(current_account)

            with patch('builtins.print', new_callable=MagicMock) as mock_print:
                bank.update_accounts()

                self.assertEqual(savings_account.get_balance(), 1050.0)

                self.assertEqual(current_account.get_balance(), 500.0)

                mock_print.assert_called_with(f"Overdraft Letter sent for Account {current_account.get_account_number()}")

if __name__ == '__main__':
    unittest.main()
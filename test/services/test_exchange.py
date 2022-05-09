from unittest import TestCase
from unittest.mock import patch

from services.exchange import Exchange


class TestExchangeService(TestCase):
    @classmethod
    def setUpClass(self):
        self.exchange = Exchange()

    @patch('utils.client.client.account')
    def test_account_balance(self, account):
        account.return_value = {'totalWalletBalance': "2000"}
        account_balance = self.exchange.account_balance()

        self.assertEqual(account_balance, 2000)

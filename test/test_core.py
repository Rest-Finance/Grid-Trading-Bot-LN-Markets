import time
from unittest import TestCase
from unittest.mock import patch

from app.bot import Bot
from utils.config import CONSTANTS


class TestCoreBot(TestCase):
    @classmethod
    def setUpClass(self):
        self.patch_account = patch('utils.client.client.account', return_value={
            "totalWalletBalance": 4000})
        self.patch_account.start()
        self.bot = Bot()
        while not self.bot.ticker.last_price:
            time.sleep(0.05)

    @classmethod
    def tearDownClass(self):
        patch.stopall()

    def test_set_quantity(self):
        self.bot.set_quantity()

        self.assertEqual(self.bot.quantity, 6.0)

    def test_should_order_when_init(self):
        self.bot.ticker._step_price = None
        self.assertEqual(self.bot.should_order(), True)

    def test_should_order_depend_step_price(self):
        self.bot.ticker._step_price = self.bot.ticker.last_price

        self.assertEqual(self.bot.should_order(), False)

        self.bot.ticker._step_price = self.bot.ticker.last_price * \
            (1.001 + CONSTANTS.limit_rate)

        self.assertEqual(self.bot.should_order(), True)

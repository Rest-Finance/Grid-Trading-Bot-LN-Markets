from unittest import TestCase

from utils.config import CONSTANTS

from services.order import hedge


class MockedExchange():
    called_times = 0

    def order(self, **kwargs):
        self.called_times += 1


class TestOrderService(TestCase):
    mockedExchange = MockedExchange()

    def tearDown(self) -> None:
        self.mockedExchange.called_times = 0

    def test_hedge(self):
        positions_allow_to_trade = {
            CONSTANTS.long: True,
            CONSTANTS.short: True
        }
        hedge(positions_allow_to_trade=positions_allow_to_trade,
              exchange=self.mockedExchange)
        
        self.assertEqual(self.mockedExchange.called_times, 2)

    def test_hedge_allow_long(self):
        positions_allow_to_trade = {
            CONSTANTS.long: True,
            CONSTANTS.short: False
        }
        hedge(positions_allow_to_trade=positions_allow_to_trade,
              exchange=self.mockedExchange)
        
        self.assertEqual(self.mockedExchange.called_times, 1)

    def test_hedge_allow_short(self):
        positions_allow_to_trade = {
            CONSTANTS.long: False,
            CONSTANTS.short: True
        }
        hedge(positions_allow_to_trade=positions_allow_to_trade,
              exchange=self.mockedExchange)
        
        self.assertEqual(self.mockedExchange.called_times, 1)

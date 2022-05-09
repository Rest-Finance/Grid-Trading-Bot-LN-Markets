from unittest import TestCase, mock
from unittest.mock import patch

from utils.config import CONSTANTS

from services.positions import set_positions_allow_to_trade


class MockedEchange:
    new_orders = []

    def __init__(self, positions) -> None:
        self._positions = positions

    def positions(self):
        return self._positions


class TestTakeProfitLevels(TestCase):
    def test_shorting_is_forbidden(self):
        positions = [{
            'positionSide': CONSTANTS.short,
            "entryPrice": 100,
            "positionAmt": "41",
            "symbol": CONSTANTS.symbol
        }, {
            'positionSide': CONSTANTS.long,
            "entryPrice": 100,
            "positionAmt": "39",
            "symbol": CONSTANTS.symbol
        }]
        mockedEchange = MockedEchange(positions=positions)
        positions_allow_to_trade = set_positions_allow_to_trade(
            exchange=mockedEchange, quantity=5)
        self.assertEqual(positions_allow_to_trade[CONSTANTS.short], False)
        self.assertEqual(positions_allow_to_trade[CONSTANTS.long], True)

    def test_bot_sides_are_forbidden(self):
        positions = [{
            'positionSide': CONSTANTS.short,
            "entryPrice": 100,
            "positionAmt": "41",
            "symbol": CONSTANTS.symbol
        }, {
            'positionSide': CONSTANTS.long,
            "entryPrice": 100,
            "positionAmt": "41",
            "symbol": CONSTANTS.symbol
        }]
        mockedEchange = MockedEchange(positions=positions)
        positions_allow_to_trade = set_positions_allow_to_trade(
            exchange=mockedEchange, quantity=5)
        self.assertEqual(positions_allow_to_trade[CONSTANTS.short], False)
        self.assertEqual(positions_allow_to_trade[CONSTANTS.long], False)

    def test_bot_sides_are_allowed(self):
        positions = [{
            'positionSide': CONSTANTS.short,
            "entryPrice": 100,
            "positionAmt": "39",
            "symbol": CONSTANTS.symbol
        }, {
            'positionSide': CONSTANTS.long,
            "entryPrice": 100,
            "positionAmt": "39",
            "symbol": CONSTANTS.symbol
        }]
        mockedEchange = MockedEchange(positions=positions)
        positions_allow_to_trade = set_positions_allow_to_trade(
            exchange=mockedEchange, quantity=5)
        self.assertEqual(positions_allow_to_trade[CONSTANTS.short], True)
        self.assertEqual(positions_allow_to_trade[CONSTANTS.long], True)

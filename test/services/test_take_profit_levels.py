from unittest import TestCase, mock
from unittest.mock import patch

from utils.config import CONSTANTS

from services.take_profit_levels import (replace_take_profit_levels,
                                         should_cancel_orders,
                                         take_profit_levels)


class MockedExchange:
    new_orders = []

    def __init__(self, positions, orders) -> None:
        self._positions = positions
        self._orders = orders

    def orders(self):
        return self._orders

    def positions(self):
        return self._positions

    def cancel_open_orders(self):
        return None

    def new_order(self, **kwargs):
        self.new_orders.append(kwargs)


class TestTakeProfitLevels(TestCase):
    def test_should_cancel_orders(self):
        positions = [{"positionAmt": "-4.3"}]
        orders = [{"origQty": "4.2"}]
        response = should_cancel_orders(positions=positions, orders=orders)

        self.assertEqual(response, True)

    def test_should_not_cancel_orders(self):
        positions = [{"positionAmt": "-4.3"}]
        orders = [{"origQty": "4.3"}]
        response = should_cancel_orders(positions=positions, orders=orders)

        self.assertEqual(response, False)

    def test_set_take_profit_levels(self):
        positions = [{
            'positionSide': CONSTANTS.short,
            "entryPrice": 100,
            "positionAmt": "2"
        }]
        orders = take_profit_levels(positions=positions)

        self.assertEqual(len(orders), len(positions))
        take_profit_price = positions[0]["entryPrice"] * \
            (1 - CONSTANTS.limit_rate)
        order = orders[0]
        expected_order = {'symbol': 'DOTUSDT',
                          'side': 'BUY',
                          'positionSide': 'SHORT',
                          'type': 'TAKE_PROFIT',
                          'timeInForce': 'GTC',
                          'quantity': float(positions[0]["positionAmt"]),
                          'price': take_profit_price,
                          'stopPrice': take_profit_price}

        self.assertEqual(order, expected_order)

    def test_replace_take_profit_levels(self):
        positions = [{
            'positionSide': CONSTANTS.short,
            "entryPrice": 100,
            "positionAmt": "2"
        }]
        orders = [{"origQty": "4.3"}]

        mockedExchange = MockedExchange(positions=positions, orders=orders)
        replace_take_profit_levels(exchange=mockedExchange)
        new_orders = mockedExchange.new_orders

        self.assertEqual(len(new_orders), 1)
        take_profit_price = mockedExchange._positions[0]["entryPrice"] * \
            (1 - CONSTANTS.limit_rate)
        expected_order = {'symbol': 'DOTUSDT',
                          'side': 'BUY',
                          'positionSide': 'SHORT',
                          'type': 'TAKE_PROFIT',
                          'timeInForce': 'GTC',
                          'quantity': float(mockedExchange._positions[0]["positionAmt"]),
                          'price': take_profit_price,
                          'stopPrice': take_profit_price}

        self.assertEqual(new_orders[0], expected_order)

    def test_not_replace_take_profit_levels(self):
        positions = [{
            'positionSide': CONSTANTS.short,
            "entryPrice": 100,
            "positionAmt": "4.3"
        }]
        orders = [{"origQty": "4.3"}]

        mockedExchange = MockedExchange(positions=positions, orders=orders)
        replace_take_profit_levels(exchange=mockedExchange)
        new_orders = mockedExchange.new_orders

        self.assertEqual(len(new_orders), 0)

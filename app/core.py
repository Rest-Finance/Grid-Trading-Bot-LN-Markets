from services.exchange import Exchange
from services.ticker import ticker
from utils.config import CONSTANTS, LoggingConfig


class CoreBot:
    quantity = CONSTANTS.quantity
    exchange = Exchange()
    ticker = ticker

    def __init__(self) -> None:
        self.set_quantity()

    def set_quantity(self):
        account_balance = self.exchange.account_balance()
        self.quantity = int(
            account_balance * CONSTANTS.quantity_balance_ratio)

    def should_order(self):
        return self.ticker.last_price and (
            not self.ticker.step_price
            or (
                self.ticker.step_price *
                (1 + CONSTANTS.limit_rate) <= self.ticker.last_price
                or self.ticker.step_price * (1 - CONSTANTS.limit_rate) >= self.ticker.last_price
            )
        )

    def run(self):
        pass

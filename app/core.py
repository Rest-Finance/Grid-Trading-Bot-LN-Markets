from services.exchange import Exchange
from services.ticker import ticker
from utils.config import CONSTANTS, LoggingConfig, api_url

LoggingConfig(log_file="logs/bot.log")


class CoreBot:
    positions_allow_to_trade = None
    print(api_url)
    quantity = CONSTANTS.quantity
    exchange = Exchange()
    ticker = ticker

    def __init__(self) -> None:
        self.set_quantity()

    def set_quantity(self):
        account_balance = self.exchange.account_balance()
        self.quantity = round(
            account_balance * CONSTANTS.quantity_balance_ratio, 1)

    def should_order(self):
        return self.ticker.last_price and (
            not self.ticker._step_price
            or (
                self.ticker._step_price *
                (1 + CONSTANTS.limit_rate) <= self.ticker.last_price
                or self.ticker._step_price * (1 - CONSTANTS.limit_rate) >= self.ticker.last_price
            )
        )

    def control_position_size(self):
        pass

    def run(self):
        pass

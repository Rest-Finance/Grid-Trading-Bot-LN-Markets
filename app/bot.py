import time

import services.order
import services.positions
from core import CoreBot
from utils.config import LoggingConfig

LoggingConfig(log_file="logs/bot.log")


class Bot(CoreBot):
    def control_position_size(self):
        while True:
            self.positions_allow_to_trade = services.positions.set_positions_allow_to_trade(
                exchange=self.exchange, quantity=self.quantity)
            time.sleep(10)

    def run(self):
        while True:
            if not self.positions_allow_to_trade:
                continue

            if self.should_order():
                self.ticker._step_price = self.ticker.last_price
                services.order.hedge(
                    positions_allow_to_trade=self.positions_allow_to_trade,
                    exchange=self.exchange,
                    ticker_price=self.ticker.last_price,
                    quantity=self.quantity
                )
            time.sleep(1)

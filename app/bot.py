import time

import services.order
from core import CoreBot
from utils.config import LoggingConfig

LoggingConfig(log_file="logs/bot.log")


class Bot(CoreBot):
    def run(self):
        while True:
            if self.should_order():
                self.ticker.step_price = self.ticker.last_price
                services.order.hedge(
                    exchange=self.exchange,
                    ticker_price=self.ticker.last_price,
                    quantity=self.quantity
                )
            time.sleep(1)

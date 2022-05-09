import logging
import os

from dotenv import load_dotenv

load_dotenv()


class ENV:
    core_api_url = os.environ.get('CORE_API_URL')


api_url = f"{ENV.core_api_url}/api/exchanges/lnmarkets"


class URL:
    balance = f"{api_url}/balance"
    positions = f"{api_url}/positions"
    order = f"{api_url}/order"


class METHODS:
    get = "GET"
    post = "POST"


class CONSTANTS:
    quantity = 1
    quantity_balance_ratio = 0.0060
    limit_rate = 0.005
    n_max_rebuy = 8
    short = "SHORT"
    long = "LONG"
    buy = "BUY"
    sell = "SELL"
    leverage = 10


class LoggingConfig:
    def __init__(self, log_file=None, logger_name="EarthBot") -> None:
        logging.basicConfig(
            filename=log_file,
            filemode="a",
            format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )

        self.logger = logging.getLogger(logger_name)

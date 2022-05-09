import logging
import os

from dotenv import load_dotenv

load_dotenv()


class ENV:
    WS_url = os.environ.get('LNM_WS_URL')
    lnm_key = os.environ.get('LNM_API_KEY')
    lnm_secret =  os.environ.get('LNM_API_SECRET')
    lnm_passphrase =  os.environ.get('LNM_PASSPHRASE')


class CONSTANTS:
    quantity = 1
    quantity_balance_ratio = 0.0060
    limit_rate = 0.01
    buy = "b"
    sell = "s"
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

import logging

import requests
from utils.config import CONSTANTS, METHODS, URL


class Exchange:
    def __handle_request(self, url: str, method: str, body=None, params=None):
        r = None
        if method == METHODS.get:
            r = requests.get(url, params=params)

        elif method == METHODS.post:
            r = requests.post(url, data=body)

        return r.json()

    def account_balance(self):
        return self.__handle_request(url=URL.balance, method=METHODS.get)['balance']

    def order(self, side: str, quantity, tp: float):
        params = {
            "type": "m",
            "side": side,
            "margin": quantity,
            "leverage": CONSTANTS.leverage,
            "takeprofit": tp
        }
        self.new_order(**params)

    def new_order(self, **kwargs):
        logging.info(kwargs)
        self.__handle_request(
            url=URL.order,
            method=METHODS.post,
            body=kwargs
        )

    def positions(self):
        return self.__handle_request(
            url=URL.positions,
            method=METHODS.get
        )

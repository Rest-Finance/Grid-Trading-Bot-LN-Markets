import json

from lnmarkets import rest
from utils.config import CONSTANTS, ENV


class Exchange:
    lnm = rest.LNMarketsRest(
        key=ENV.lnm_key, secret=ENV.lnm_secret, passphrase=ENV.lnm_passphrase)

    def account_balance(self):
        user = json.loads(self.lnm.get_user())

        return user['balance'] + user['total_running_margin']

    def order(self, side: str, quantity: int, tp: float):
        self.lnm.futures_new_position({
            'type': 'm',
            'side':  side,
            'margin': quantity,
            'leverage': CONSTANTS.leverage,
            'takeprofit': tp
        })

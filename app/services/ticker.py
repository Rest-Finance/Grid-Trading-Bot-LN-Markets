import json

from utils.config import ENV
from websocket import create_connection


class Ticker:
    last_price = None
    step_price = None

    def start(self) -> None:
        ws = create_connection(ENV.WS_url)
        ws.send(
            '{"method":"subscribe", "jsonrpc": "2.0", "params": ["futures/market/index"]}')

        while True:
            data = json.loads(ws.recv())
            if 'method' in data and data['method'] == 'futures/market/index':
                self.last_price = data['params']['index']

ticker = Ticker()

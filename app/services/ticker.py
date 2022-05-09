import logging
import time

import socketio
from utils.config import ENV

sio = socketio.Client()


class Ticker:
    last_price = None
    _step_price = None
    _connected = False

    def start(self) -> None:
        while not self._connected:
            try:
                sio.connect(ENV.core_api_url)
                self._connected = True
                logging.info('[ OK ] Websocket connection established')
                sio.wait()
            except:
                logging.error('[ ! ] Websocket connection failed')
                time.sleep(10)


ticker = Ticker()


@sio.event
def lnmarketsticker(data):
    ticker.last_price = data

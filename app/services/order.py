from utils.config import CONSTANTS


def hedge(exchange, ticker_price,  quantity=CONSTANTS.quantity):
    exchange.order(side=CONSTANTS.buy, quantity=quantity,
                   tp=int(ticker_price * (1 + CONSTANTS.limit_rate)))

    exchange.order(side=CONSTANTS.sell, quantity=quantity,
                   tp=int(ticker_price * (1 - CONSTANTS.limit_rate)))

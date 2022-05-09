from time import clock_getres

from utils.config import CONSTANTS


def hedge(positions_allow_to_trade, exchange, ticker_price,  quantity=CONSTANTS.quantity):
    if positions_allow_to_trade[CONSTANTS.long]:
        tp = ticker_price * (1 + CONSTANTS.limit_rate)
        exchange.order(side="b", quantity=quantity, tp=tp)
    if positions_allow_to_trade[CONSTANTS.short]:
        tp = ticker_price * (1 - CONSTANTS.limit_rate)
        exchange.order(side="s", quantity=quantity, tp=tp)

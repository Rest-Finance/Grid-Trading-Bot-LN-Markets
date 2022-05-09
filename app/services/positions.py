import logging

from utils.config import CONSTANTS


def set_positions_allow_to_trade(exchange, quantity=CONSTANTS.quantity):
    try:
        positions = exchange.positions()
    except:
        logging.warning("[ ! ] exchange.positions failed")
        return {CONSTANTS.long: False, CONSTANTS.short: False}

    positions_allow_to_trade = {
        CONSTANTS.long: True, CONSTANTS.short: True}

    longAmount = 0
    shortAmount = 0

    for position in positions:
        if position['side'] == "b":
            longAmount += position["margin"]
        elif position['side'] == "s":
            shortAmount += position["margin"]

    if longAmount > CONSTANTS.n_max_rebuy * quantity:
        positions_allow_to_trade[CONSTANTS.long] = False

    elif shortAmount > CONSTANTS.n_max_rebuy * quantity:
        positions_allow_to_trade[CONSTANTS.short] = False

    return positions_allow_to_trade

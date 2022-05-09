import threading

from bot import Bot
from services.ticker import ticker


def main():
    bot = Bot()
    threading.Thread(target=bot.run).start()
    threading.Thread(target=ticker.start).start()
    threading.Thread(target=bot.control_position_size).start()


if __name__ == "__main__":
    main()

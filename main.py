import sys

from bot import Bot
from utils import log


if sys.stdout.encoding == 'cp1251':
    sys.stdout.reconfigure(encoding='utf-8')


bot = Bot('Вадим')


def main():
    print('\v\v')
    response = bot.say_hello()

    while response is None:
        response = bot.trying_to_chat(response)

    while response is not None:
        response = bot.connect_continue(bot.clean_data(response))


if __name__ == '__main__':
    main()

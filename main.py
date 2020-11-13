import sys

# from protobot import Bot
from bot import Bot


if sys.stdout.encoding == 'cp1251':
    sys.stdout.reconfigure(encoding='utf-8')

name = input('To test me, enter your name: ')

def main():
    print('\v\v')

    bot = Bot()
    response = bot.say_hello(name)

    while bot:

        while response is None:
            response = bot.trying_to_chat(response)

        while response is not None:
            response = bot.chat_continue(response)


if __name__ == '__main__':
    main()

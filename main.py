from bot import Bot
from utils import set_utf8_if_cp


set_utf8_if_cp()

name = input('To test me, enter your name: ')

def main():
    bot = Bot()
    response = bot.say_hello(name)

    while bot:

        while response is None:
            response = bot.trying_to_chat(response)

        while response is not None:
            response = bot.chat_continue(response)

if __name__ == '__main__':
    main()
 
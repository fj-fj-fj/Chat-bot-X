"""
This module is an alternative to the `main` module. The essence is the same.

"""
import sys

from INTERACTION import BOT_PHRASES, Logic, goto
from utils import time_input, set_utf8_if_cp


set_utf8_if_cp()

logic = Logic.HELLO.value

repeat = False


def say_hello(name):
    hello = BOT_PHRASES["hello"]
    return time_input(hello.format(name.capitalize()))


def chat(response):
    global logic, repeat

    if response is None:

        if not repeat:
            repeat = True
            phrase, logic = goto['null'][logic]
            return time_input(phrase)
        phrase, _ = goto['null'][None]
        raise sys.exit(phrase)

    repeat = response is not None

    if response.isdigit() and logic == Logic.MAIN.value:

        if int(response) in range(9):
            phrase, _ = goto['bad']
        elif int(response) in range(9, 11):
            phrase, _ = goto['good']
        raise sys.exit(phrase)

    if response not in goto.keys():
        phrase, logic = goto['default'][logic]
        return time_input(phrase)

    for key in goto:

        if isinstance(goto[response], dict):
            phrase, logic = goto[response][logic]
        elif isinstance(goto[response], tuple):
            phrase, logic = goto[response]

        if logic == Logic.HANGUP.value:
            raise sys.exit(phrase)
        return time_input(phrase)
    raise sys.exit('some error')


def main():
    name = input('To test me, enter your name: ')
    response = say_hello(name)

    while True:
        response = chat(response)


if __name__ == '__main__':
    main()

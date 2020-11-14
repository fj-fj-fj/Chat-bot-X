"""This module is an alternative to the `main` module. The essence is the same.

"""
# Был модифицирован объект `goto`, добавлением в него указателей перехода
# к следуюей логике: hello_logic -> 1, main_logic -> 2, завершить программу -> 0.
# Это позволило сократить кол-во кода и, кажется, скрипт стал более читаем


import sys

from phrases.interaction import BOT_PHRASES
from utils import time_input

if sys.stdout.encoding == 'cp1251':
    sys.stdout.reconfigure(encoding='utf-8')


goto = {
    'null': {
        1: (BOT_PHRASES.get('hello_null'), 1),
        2: (BOT_PHRASES.get('recommend_null'), 2),
        None: (BOT_PHRASES.get('hangup_null'), 0)
    },
    'да': {
        1: (BOT_PHRASES.get('recommend_main'), 2),
        2: (BOT_PHRASES.get('recommend_score_positive'), 2)
    },
    'нет': {
        1: (BOT_PHRASES.get('hangup_wrong_time'), 0),
        2: (BOT_PHRASES.get('recommend_score_negative'), 2)
    },
    'занят': (BOT_PHRASES.get('hangup_wrong_time'), 0),
    'не знаю': (BOT_PHRASES.get('recommend_repeat_2'), 2),
    'возможно': (BOT_PHRASES.get('recommend_score_neutral'), 2),
    'еще раз': {
        1: (BOT_PHRASES.get('hello_repeat'), 1),
        2: (BOT_PHRASES.get('recommend_repeat'), 2)
    },
    '?': (BOT_PHRASES.get('forward'), 2),  # nlu
    'bad': (BOT_PHRASES.get('hangup_negative'), 0),
    'good': (BOT_PHRASES.get('hangup_positive'), 0),
    'default': {
        1: (BOT_PHRASES.get('recommend_main'), 2),
        2: (BOT_PHRASES.get('recommend_default'), 2)
    }
}

logic = 1
repeat = False
connecting = logic is True


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

    if response.isdigit() and logic == 2:

        if int(response) in range(8):
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

        if not logic:
            raise sys.exit(phrase)

        return time_input(phrase)

    raise sys.exit('some error')


name = input('To test me, enter your name: ')


def main():

    response = say_hello(name)

    while True:

        response = chat(response)


if __name__ == '__main__':
    main()

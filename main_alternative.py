"""This module is an alternative to the `main` module. The essence is the same.
    
    import:
    1. Enum: Logic - bot next action pointers
    2. phrases.interaction.bot_phrases - bot behavior patterns
       contains:
          hello_* : the logic of starting a conversation with a person
          recommend_* : base logic (clarification of service quality assessment)
          hangup_* : conversation termination logic
    3. utils.time_input - input() with a lifespan of 5 seconds
    4. utils.set_utf8_if_cp - set utf-8 if cp1251 is default
    
    goto.keys() - human behavior patterns
    goto.values() - typles: (bot pattern, the next step for the bot), (), () ...
    func: chat - processes the human response
        
"""
# в объект `goto` добавлены перечисления, для оснований следующего действия бота
import sys
from enum import Enum

from INTERACTION import interaction
from utils import time_input, set_utf8_if_cp


set_utf8_if_cp()

BOT_PHRASES = interaction.bot_phrases

Logic = Enum('Logic', 'HANGUP HELLO MAIN', start=0)

goto = {
    'null': {
        1: (BOT_PHRASES.get('hello_null'), Logic.HELLO.value),
        2: (BOT_PHRASES.get('recommend_null'), Logic.MAIN.value),
        None: (BOT_PHRASES.get('hangup_null'), Logic.HANGUP.value)
    },
    'да': {
        1: (BOT_PHRASES.get('recommend_main'), Logic.MAIN.value),
        2: (BOT_PHRASES.get('recommend_score_positive'), Logic.MAIN.value)
    },
    'нет': {
        1: (BOT_PHRASES.get('hangup_wrong_time'), Logic.HANGUP.value),
        2: (BOT_PHRASES.get('recommend_score_negative'), Logic.MAIN.value)
    },
    'занят': (BOT_PHRASES.get('hangup_wrong_time'), Logic.HANGUP.value),
    'не знаю': (BOT_PHRASES.get('recommend_repeat_2'), Logic.MAIN.value),
    'возможно': (BOT_PHRASES.get('recommend_score_neutral'), Logic.MAIN.value),
    'еще раз': {
        1: (BOT_PHRASES.get('hello_repeat'), Logic.HELLO.value),
        2: (BOT_PHRASES.get('recommend_repeat'), Logic.MAIN.value)
    },
    '?': (BOT_PHRASES.get('forward'), Logic.MAIN.value),  # nlu
    'bad': (BOT_PHRASES.get('hangup_negative'), Logic.HANGUP.value),
    'good': (BOT_PHRASES.get('hangup_positive'), Logic.HANGUP.value),
    'default': {
        1: (BOT_PHRASES.get('recommend_main'), Logic.MAIN.value),
        2: (BOT_PHRASES.get('recommend_default'), Logic.MAIN.value)
    }
}

logic = Logic.HELLO.value

repeat = False

def say_hello(name):
    hello = BOT_PHRASES["hello"]
    return time_input(hello.format(name.capitalize()))

def chat(response):
    """Processes the human response.

    response is None - human ignores
    response.isdigit and logic.MAIN - assesses the quality of service
    response not in goto.keys - the answer is incomprehensible
    for key in goto - other behavior patterns

    """
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
 
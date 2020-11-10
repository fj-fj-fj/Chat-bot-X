import sys

from bot import Bot
from utils import log


if sys.stdout.encoding == 'cp1251':
    sys.stdout.reconfigure(encoding='utf-8')


bot = Bot('Вадим')

# if IN: есть тут кто?; and OUT: [eerie grunting]:
default = bot.recommend_main, bot.recommend_default

goto = {
    'null': {
        'hello_null': bot.hello_null,
        'recommend_null': bot.recommend_null, 
        'hangup_null': bot.hangup_null
    },
    'да': {
        'recommend_main': bot.recommend_main,
        'recommend_score_positive': bot.recommend_score_positive
    },
    'нет': {
        'hangup_wrong_time': bot.hangup_wrong_time,
        'recommend_score_negative': bot.recommend_score_negative
    },
    'занят': bot.hangup_wrong_time,
    'не знаю': bot.recommend_repeat_2,
    'возможно': bot.recommend_score_neutral,
    'еще раз': {
        'hello_repeat': bot.hello_repeat, 
        'recommend_repeat': bot.recommend_repeat
    },
    '?': bot.forward,
    'bad': [range(9), bot.hangup_negative],
    'good': [range(9, 11), bot.hangup_positive],
    'exit': [
        'hangup_null', 'hangup_positive',
        'hangup_negative','hangup_wrong_time',
    ]
}

def clean_data(response):
    if isinstance(response, int):
        response = str(response)
    return response.lower().strip()


def get_current_logic():
    global default
    if bot.HELLOLOGIC:
        default_ = default[0]
    elif bot.MAINLOGIC:
        default_ = default[1]
    return default_


def score_on_a_scale_of_1_to_10(n):
    good = goto.get('good')
    bad = goto.get('bad')

    if int(n) in good[0]:
        func = good[1]
    elif int(n) in bad[0]:
        func = bad[1]
    return func


def start():
    print('\v\v')
    response = bot.say_hello()

    while response is None:
        response = trying_to_chat(response)

    response = connect_continue(clean_data(response))

    while response is not None:
        response = connect_continue(clean_data(response))


def trying_to_chat(response):
    print(log[0].format(response))
    user_null = response is None

    if user_null:
        # юзер молчит, проверим, был ли повторный звонок
        bot.repeated = True if not bot.repeated else False
    ask_again = bot.repeated

    # игнор; main/hello логика; попытка связаться:
    if user_null and bot.HELLOLOGIC and ask_again:
        func = goto['null']['hello_null']
    elif user_null and bot.MAINLOGIC and ask_again:
        func = goto['null']['recommend_null']
    elif user_null and (bot.HELLOLOGIC or bot.MAINLOGIC) and not ask_again:
        func = goto['null']['hangup_null']

    connect = func.__name__ not in goto['exit']
    print(log[1].format(func.__name__))

    if not connect: func(); raise sys.exit()
    return func()


def connect_continue(response):
    print(log[2].format(response))

    # проверим, есть ли ответ юзера в нашем списке юзерских фраз:
    coincidence = any(list(filter(lambda x: x == response, list(goto.keys()))))

    try:
        if bot.HELLOLOGIC and coincidence:
            key = list(goto.get(response).keys())[0]

        elif bot.MAINLOGIC and (coincidence or response.isdigit()):
            # проверим сразу на наличие оценки:
            if response.isdigit():
                if int(response) in range(11):
                    end = score_on_a_scale_of_1_to_10(response)()
                    raise sys.exit()

            key = list(goto.get(response).keys())[1]

        default = get_current_logic()
        func = goto[response].get(key, default)
    except (KeyError, AttributeError):
        default = get_current_logic()
        func = goto.get(response, default)
    
    # entyty_value(если надо ...)
    
    response = func()

    while response is None:
        # молчит... мы переспросим:
        response = trying_to_chat(response)

    wrong_time = func.__name__ in goto['exit']
    if wrong_time: raise sys.exit()

    return response


if __name__ == '__main__':
    # main()
    start()

# def entity_value():
    # response = func(repeat=True) if response == 'еще раз'
    # response = func(wrong_time=True) if response == 'занят'
    # response = func(confirm=True) if bot.HELLOLOGIC else func()
    # response = func(confirm=False) if bot.HELLOLOGIC and response == 'нет'
    # response = func(recommendation_score=[0..8]) if response == '0-8'
    # response = func(recommendation_score=[9..10]) if response == '9-10'
    # response = func(recommendation=negative) if bot.MAINLOGIC and response == 'нет'
    # response = func(recommendation=positive) if bot.MAINLOGIC and response == 'да'
    # response = func(recommendation=neutral) if bot.MAINLOGIC and response == 'возможно'
    # response = func(repeat=True) if bot.MAINLOGIC and response == 'еще раз'
    # response = func(recommendation=dont_now) if bot.MAINLOGIC and response == 'не знаю'
    # response = func(question=True) if response == '?'
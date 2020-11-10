import sys

from bot import Bot
from utils import get_func_name
from utils import inspect_func


if sys.stdout.encoding == 'cp1251':
    sys.stdout.reconfigure(encoding='utf-8')


bot = Bot('Вадим')
# флаг для повторных звоноков:
repeated = False

goto = {
    True: bot.hello_null,
    False: bot.hangup_null, 
    'да': bot.recommend_main, 
    'нет': bot.hangup_wrong_time,
    'занят': bot.hangup_wrong_time,
    'еще раз': bot.hello_repeat
}

# IN: есть тут кто?;  OUT: [eerie grunting]
default = bot.recommend_main


def start():
    # пробуем установить связь:
    response = bot.say_hello()
    while response is None:
        # юзер молчит и повторный звонок еще не был совершен
        # воспользуемся флагом повтора:
        second_time = cur_state(response)
        print('-----1', second_time)
        # 2й звонок (null или иное):
        response = trying_to_chat(second_time)
        print('----------2', response)
    # есть контакт!
    response = connect_continue(clean_data(response))
    while response is not None:
        print('----------------3', response)
        response = connect_continue(clean_data(response))


def cur_state(response):
    print('from cur_state')
    if response is None:
        global repeated
        repeated = True if not repeated else False
        return repeated


def trying_to_chat(response):
    print('from trying_to_chat')
    func = goto.get(response, default)
    connect = func.__name__ != 'hangup_null'
    print('*****1', func.__name__)
    if not connect:
        # если не задалось, заканчиваем монолог:
        print('**********2', connect)
        raise sys.exit(f'{func()}')
    print('***************3')
    return func()


def clean_data(response):
    # очистимся
    print('clean_data')
    if isinstance(response, int):
        response = str(response)
    return response.lower().strip()


def connect_continue(response):
    print('from connect_continue')
    func = goto.get(response, default)
    response = func()
    while response is None:
        # молчит... воспользуемся флагом повтора:
        second_time = cur_state(response)
        # и переспросим:
        response = trying_to_chat(second_time)
    wrong_time = func.__name__ == 'hangup_wrong_time'
    if wrong_time:
        raise sys.exit()
    print('no exit')
    return response


if __name__ == '__main__':
    # main()
    start()
    print('^^^^^^^^^^^^  end   ^^^^^^^^^^^^^^^')

""" initial draft, hasty naming, Windows needles, etc """

import re
import sys

from utils import print
from utils import time_input
from utils import log


pattern = r'((?!\n)\s+)'

INTENTIONS = {
    "hello":

            re.sub(pattern, ' ', """{},  добрый день! Вас беспокоит компания X, мы проводим опрос 
            удовлетворенности нашими услугами. Подскажите, вам удобно сейчас говорить?"""),

    "hello_repeat":

            "Это компания X  Подскажите, вам удобно сейчас говорить?",

    "hello_null":

            "Извините, вас не слышно. Вы могли бы повторить?",

    "hangup_positive":

            "Отлично! Большое спасибо за уделенное время! Всего вам доброго!",
            
    "hangup_negative":

            "Я вас понял. В любом случае большое спасибо за уделенное время! Всего вам доброго.",

    "hangup_wrong_time":

            "Извините пожалуйста за беспокойство. Всего вам доброго",

    "hangup_null":

            "Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго",

    "forward": 

            "Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. Пожалуйста оставайтесь на линии.",

    "recommend_main":

            re.sub(pattern, ' ', """Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, 
            по шкале от «0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую."""),

    "recommend_repeat":

            re.sub(pattern, ' ', """Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0 до 10, 
            где 0 - точно не порекомендую, 10 - обязательно порекомендую?"""),

    "recommend_repeat_2":

            re.sub(pattern, ' ', """Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, 
            вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0»"""),

    "recommend_score_negative":

            "Ну а от 0 до 10 как бы вы оценили бы: 0, 5, или может, 7 ?",

    "recommend_score_neutral":

            "Ну а от 0 до 10 как бы вы оценили ?",

    "recommend_score_positive":

            "Хорошо, а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10?",

    "recommend_null":

            "Извините вас свосем не слышно, повторите пожалуйста",

    "recommend_default": 

            "повторите пожалуйста"

}


class ChatLogic:

    HELLOLOGIC = False
    MAINLOGIC = False
    repeated = False
    _indent = '\n\a\N{Robot Face}\t>>\t>>>\t'

    # ---------------  HelloLogic:  -----------------------
    @staticmethod
    def say_hello(name):
        ChatLogic.MAINLOGIC = False
        ChatLogic.HELLOLOGIC = True
        hello = INTENTIONS["hello"]
        hello = f'{ChatLogic._indent}{hello}\n\n'
        return time_input(hello.format(name))

    @staticmethod
    def hello_repeat(repeat=None):
        ChatLogic.MAINLOGIC = False
        ChatLogic.HELLOLOGIC = True
        re_ask = INTENTIONS["hello_repeat"]
        re_ask = f'{ChatLogic._indent}{re_ask}\n\n'
        return time_input(re_ask)

    @staticmethod
    def hello_null():
        ChatLogic.MAINLOGIC = False
        ChatLogic.HELLOLOGIC = True
        see_you = INTENTIONS["hello_null"]
        see_you = f'{ChatLogic._indent}{see_you}\n\n'
        return time_input(see_you)

    # ---------------  HangupLogic:  -----------------------
    @staticmethod
    def hangup_positive(recommendation_score=None):
        hangup = INTENTIONS["hangup_positive"]
        print(hangup)
        return hangup
        # yield hangup
        # other hangup action ...
    
    @staticmethod
    def hangup_negative(recommendation_score=None):
        hangup = INTENTIONS["hangup_negative"]
        print(hangup)
        return hangup
        # yield hangup
        # other hangup action ...
    
    @staticmethod
    def hangup_wrong_time(confirm=None, wrong_time=None):
        hangup = INTENTIONS["hangup_wrong_time"]
        print(hangup)
        return hangup
        # yield hangup
        # other hangup action ...

    @staticmethod
    def hangup_null():
        ill_be_back = INTENTIONS["hangup_null"]
        print(ill_be_back, end='\N{Winking Face}\n')
        return ill_be_back
        # yield ill_bi_back
        # other hangup action ...

    # ---------------  ForwardLogic:  -----------------------
    @staticmethod
    def forward(question=None):
        wait_skin = INTENTIONS["forward"]
        stay_on_line = f'{ChatLogic._indent}{wait_skin}\n\n'
        print(stay_on_line)
        return stay_on_line
        # yield stay_on_line
        # other bring action ...
    
    # ---------------  MainLogic:  -----------------------
    @staticmethod
    def recommend_main(confirm=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        rate_me = INTENTIONS["recommend_main"]
        rate_me = f'{ChatLogic._indent}{rate_me}\n\n'
        return time_input(rate_me)

    @staticmethod
    def recommend_repeat(repeat=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        rate_me = INTENTIONS["recommend_repeat"]
        rate_me = f'{ChatLogic._indent}{rate_me}\n\n'
        return time_input(rate_me)

    @staticmethod
    def recommend_repeat_2(repeat=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        rate_me = INTENTIONS["recommend_repeat_2"]
        rate_me = f'{ChatLogic._indent}{rate_me}\n\n'
        return time_input(rate_me)

    @staticmethod
    def recommend_score_negative(recommendation=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        obsession = INTENTIONS["recommend_score_negative"]
        obsession = f'{ChatLogic._indent}{obsession}\n\n'
        return time_input(obsession)
    
    @staticmethod
    def recommend_score_neutral(recommendation=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        persistence = INTENTIONS["recommend_score_neutral"]
        persistence = f'{ChatLogic._indent}{persistence}\n\n'
        return time_input(persistence)
    
    @staticmethod
    def recommend_score_positive(recommendation=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        rate_me = INTENTIONS["recommend_score_positive"]
        insert_scale = f'{ChatLogic._indent}{rate_me}\n\n'
        return time_input(insert_scale)
    
    @staticmethod
    def recommend_null():
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        re_ask = INTENTIONS["recommend_null"]
        re_ask = f'{ChatLogic._indent}{re_ask}\n\n'
        return time_input(re_ask)

    @staticmethod
    def recommend_default():
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        re_ask = INTENTIONS["recommend_default"]
        re_ask = f'{ChatLogic._indent}{re_ask}\n\n'
        return time_input(re_ask)


class Connect(ChatLogic):

    @staticmethod
    def clean_data(response):
        return response.lower().strip()


    def get_current_defаlt(self) -> callable:
        """self.HELLOLOGIC -> return recommend_main
           self.MAINLOGIC -> return recommend_default
        """

        return default[0 if self.HELLOLOGIC else 1]


    def score_on_a_scale_of_1_to_10(self, n) -> callable:
        """ User: [0...8] Bot: hangup_negative
            User: [9..10] Bot: hangup_positive
            
        """
        good = goto.get('good')
        bad = goto.get('bad')

        return bad if int(n) in range(9) else good


    def trying_to_chat(self, response) -> callable:
        """User is None:
                re-ask if not asked
                exit if it was
        
        """
        # print(log[0].format(response))
        user_null = response is None

        if user_null:
            self.repeated = True if not self.repeated else False
        re_ask = self.repeated

        if user_null and self.HELLOLOGIC and re_ask:
            func = goto['null']['hello_null']
        elif user_null and self.MAINLOGIC and re_ask:
            func = goto['null']['recommend_null']
        elif user_null and (self.HELLOLOGIC or self.MAINLOGIC) and not re_ask:
            func = goto['null']['hangup_null']

        connect = func.__name__ not in goto['exit']
        # print(log[1].format(func.__name__))

        if not connect: func(); raise sys.exit()

        return func()
    

    def chat_continue(self, response) -> callable:
        """If user replied: goto: {response: function};
           if rated: exit; if null: re-ask
        
        """
        # print(log[2].format(response))
        response = Bot.clean_data(response)

        # проверим, есть ли ответ юзера в нашем списке юзерских фраз:
        coincidence = any(list(filter(lambda x: x == response, list(goto.keys()))))

        try:
            if self.HELLOLOGIC and coincidence:
                key = list(goto.get(response).keys())[0]

            elif self.MAINLOGIC and (coincidence or response.isdigit()):
                
                if response.isdigit() and int(response) in range(11):
                        self.score_on_a_scale_of_1_to_10(response)()
                        raise sys.exit()

                key = list(goto.get(response).keys())[1]

            default = self.get_current_defаlt()
            func = goto[response].get(key, default)

        except (KeyError, AttributeError):
            default = self.get_current_defаlt()
            func = goto.get(response, default)
        
        # entyty_value(если надо ...)
        
        response = func()

        wrong_time = func.__name__ in goto['exit']
        if wrong_time: raise sys.exit()

        return response


class Bot(Connect):
    
    def say_hello(self, name):
        return super().say_hello(name.capitalize())



bot = Bot

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
    'bad': bot.hangup_negative,
    'good': bot.hangup_positive,
    'exit': [
        'hangup_null', 'hangup_positive',
        'hangup_negative','hangup_wrong_time',
    ]
}
# if IN: есть тут кто?; and OUT: [eerie grunting]:
default = bot.recommend_main, bot.recommend_default


if __name__ == '__main__':
    bot = Bot('Chapa')


# ---------------  Entity/Value  -----------------------
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
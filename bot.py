import re

from utils import tinput, print


pattern = r'((?!\n)\s+)'

INTENTIONS = {
    "hello":

            re.sub(pattern, ' ', """добрый день! Вас беспокоит компания X, мы проводим опрос 
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
            где 0 - точно не порекомендую, 10 - обязательно порекомендую."""),

    "recommend_repeat_2":

            re.sub(pattern, ' ', """Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, 
            вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0»"""),

    "recommend_score_negative":

            "Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?",

    "recommend_score_neutral":

            "Ну а от 0 до 10 как бы вы оценили ?",

    "recommend_score_positive":

            "Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10?",

    "recommend_null":

            "Извините вас свосем не слышно, повторите пожалуйста",

    "recommend_default": 

            "повторите пожалуйста"

}



class ChatLogic:

    _indent = '\a>\t>\t>\t'

    # ---------------  HelloLogic:  -----------------------
    @staticmethod
    def say_hello():
        introduction = INTENTIONS["hello"]
        can_u_talk = f'{ChatLogic._indent}{introduction}\n'
        return tinput(can_u_talk)

    @staticmethod
    def hello_repeat(repeat=None):
        this_is_me = INTENTIONS["hello_repeat"]
        can_u_talk = f'{ChatLogic._indent}{this_is_me}\n'
        return tinput(can_u_talk)

    @staticmethod
    def hello_null():
        no_sound = INTENTIONS["hello_null"]
        can_u_repeat = f'{ChatLogic._indent}{no_sound}\n'
        return tinput(can_u_repeat)

    # ---------------  HangupLogic:  -----------------------
    @staticmethod
    def hangup_positive():
        intention = INTENTIONS["hangup_positive"]
        pass
    
    @staticmethod
    def hangup_negative():
        intention = INTENTIONS["hangup_negative"]
        pass
    
    @staticmethod
    def hangup_wrong_time(confirm=None, wrong_time=None):
        sorry_bye = INTENTIONS["hangup_wrong_time"]
        print(sorry_bye)
        return bye

    @staticmethod
    def hangup_null():
        ill_be_back = INTENTIONS["hangup_null"]
        print(ill_be_back, end='\N{Winking Face}\n')
        return ill_be_back

    # ---------------  ForwardLogic:  -----------------------
    @staticmethod
    def forward():
        wait_skin = INTENTIONS["forward"]
        stay_on_line = f'{ChatLogic._indent}{wait_skin}\n'
        print(stay_on_line)
        return stay_on_line
    
    # ---------------  MainLogic:  -----------------------
    @staticmethod
    def recommend_main(confirm=None):
        ask_question = INTENTIONS["recommend_main"]
        rate_us = f'{ChatLogic._indent}{ask_question}\n'
        return tinput(rate_us)

    @staticmethod
    def recommend_repeat():
        intention = INTENTIONS["recommend_repeat"]
        pass

    @staticmethod
    def recommend_repeat_2():
        intention = INTENTIONS["recommend_repeat_2"]
        pass

    @staticmethod
    def recommend_score_negative():
        intention = INTENTIONS["recommend_score_negative"]
        pass
    
    @staticmethod
    def recommend_score_neutral():
        intention = INTENTIONS["recommend_score_neutral"]
        pass
    
    @staticmethod
    def recommend_score_positive():
        intention = INTENTIONS["recommend_score_positive"]
        pass
    
    @staticmethod
    def recommend_null():
        intention = INTENTIONS["recommend_null"]
        pass

    @staticmethod
    def recommend_default():
        intention = INTENTIONS["recommend_default"]
        pass


class Bot(ChatLogic):

    def __init__(self, name='', data={}):
        self.name = name if name else f'{name}, '
        self.data = data

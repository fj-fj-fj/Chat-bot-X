import re

from utils import print
from utils import tinput


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
            где 0 - точно не порекомендую, 10 - обязательно порекомендую?"""),

    "recommend_repeat_2":

            re.sub(pattern, ' ', """Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, 
            вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0»"""),

    "recommend_score_negative":

            "Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?",

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
    _indent = '\a\N{Robot Face}\t>>\t>>>\t'

    # ---------------  HelloLogic:  -----------------------
    @staticmethod
    def say_hello():
        ChatLogic.MAINLOGIC = False
        ChatLogic.HELLOLOGIC = True
        introduction = INTENTIONS["hello"]
        can_u_talk = f'{ChatLogic._indent}{introduction}\n'
        return tinput(can_u_talk)

    @staticmethod
    def hello_repeat(repeat=None):
        ChatLogic.MAINLOGIC = False
        ChatLogic.HELLOLOGIC = True
        this_is_me = INTENTIONS["hello_repeat"]
        can_u_talk = f'{ChatLogic._indent}{this_is_me}\n'
        return tinput(can_u_talk)

    @staticmethod
    def hello_null():
        ChatLogic.MAINLOGIC = False
        ChatLogic.HELLOLOGIC = True
        no_voice = INTENTIONS["hello_null"]
        can_u_repeat = f'{ChatLogic._indent}{no_voice}\n'
        return tinput(can_u_repeat)

    # ---------------  HangupLogic:  -----------------------
    @staticmethod
    def hangup_positive(recommendation_score=None):
        great_bye = INTENTIONS["hangup_positive"]
        print(great_bye)
        return great_bye
        # yield great_bye
        # other hangup action ...
    
    @staticmethod
    def hangup_negative(recommendation_score=None):
        bad_bye = INTENTIONS["hangup_negative"]
        print(bad_bye)
        return bad_bye
        # yield great_bye
        # other hangup action ...
    
    @staticmethod
    def hangup_wrong_time(confirm=None, wrong_time=None):
        sorry_bye = INTENTIONS["hangup_wrong_time"]
        print(sorry_bye)
        return sorry_bye
        # yield great_bye
        # other hangup action ...

    @staticmethod
    def hangup_null():
        ill_be_back = INTENTIONS["hangup_null"]
        print(ill_be_back, end='\N{Winking Face}\n')
        return ill_be_back
        # yield great_bye
        # other hangup action ...

    # ---------------  ForwardLogic:  -----------------------
    @staticmethod
    def forward(question=None):
        wait_skin = INTENTIONS["forward"]
        stay_on_line = f'{ChatLogic._indent}{wait_skin}\n'
        print(stay_on_line)
        return stay_on_line
        # yield stay_on_line
        # other bring action ...
    
    # ---------------  MainLogic:  -----------------------
    @staticmethod
    def recommend_main(confirm=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        ask_question = INTENTIONS["recommend_main"]
        rate_me = f'{ChatLogic._indent}{ask_question}\n'
        return tinput(rate_me)

    @staticmethod
    def recommend_repeat(repeat=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        ask_repeat = INTENTIONS["recommend_repeat"]
        rate_me = f'{ChatLogic._indent}{ask_repeat}\n'
        return tinput(rate_me)

    @staticmethod
    def recommend_repeat_2(repeat=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        ask_repeat_2 = INTENTIONS["recommend_repeat_2"]
        rate_me = f'{ChatLogic._indent}{ask_repeat_2}\n'
        return tinput(rate_me)

    @staticmethod
    def recommend_score_negative(recommendation=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        obsession = INTENTIONS["recommend_score_negative"]
        obsession = f'{ChatLogic._indent}{obsession}\n'
        return tinput(obsession)
    
    @staticmethod
    def recommend_score_neutral(recommendation=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        persistence = INTENTIONS["recommend_score_neutral"]
        persistence = f'{ChatLogic._indent}{persistence}\n'
        return tinput(persistence)
    
    @staticmethod
    def recommend_score_positive(recommendation=None):
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        rate_me = INTENTIONS["recommend_score_positive"]
        insert_scale = f'{ChatLogic._indent}{rate_me}\n'
        return tinput(insert_scale)
    
    @staticmethod
    def recommend_null():
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        no_voice = INTENTIONS["recommend_null"]
        please_repeat = f'{ChatLogic._indent}{no_voice}\n'
        return tinput(please_repeat)

    @staticmethod
    def recommend_default():
        ChatLogic.HELLOLOGIC = False
        ChatLogic.MAINLOGIC = True
        repeat = INTENTIONS["recommend_default"]
        please = f'{ChatLogic._indent}{repeat}\n'
        return tinput(please)


class Bot(ChatLogic):

    def __init__(self, name='', data={}):
        self.name = name if name else f'{name}, '
        self.data = data


if __name__ == '__main__':
    bot = Bot('Chapa')
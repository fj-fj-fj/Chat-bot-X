import re
import sys

from utils import time_input


pattern = r'((?!\n)\s+)'

BOT_PHRASES = {
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

            "Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. Пожалуйста оставайтесь на линии.  ♫•*¨*•.¸¸♪",

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

goto = {
    'null': {
        'hello_null': BOT_PHRASES.get('hello_null'),
        'recommend_nul': BOT_PHRASES.get('recommend_null'), 
        'hangup_null': BOT_PHRASES.get('hangup_null')
    },
    'да': {
        'recommend_main': BOT_PHRASES.get('recommend_main'),
        'recommend_score_positive': BOT_PHRASES.get('recommend_score_positive')
    },
    'нет': {
        'hangup_wrong_time': BOT_PHRASES.get('hangup_wrong_time'),
        'recommend_score_negative': BOT_PHRASES.get('recommend_score_negative')
    },
    'занят': BOT_PHRASES.get('hangup_wrong_time'),
    'не знаю': BOT_PHRASES.get('recommend_repeat_2'),
    'возможно': BOT_PHRASES.get('recommend_score_neutral'),
    'еще раз': {
        'hello_repeat': BOT_PHRASES.get('hello_repeat'), 
        'recommend_repeat': BOT_PHRASES.get('recommend_repeat')
    },
    '?': BOT_PHRASES.get('forward'),
    'bad': BOT_PHRASES.get('hangup_negative'),
    'good': BOT_PHRASES.get('hangup_positive'),
    'exit': [
        'hangup_null', 'hangup_positive',
        'hangup_negative','занят',
    ]
}
# in: hey? out: [CROWLING AND SCREAMING]:
default = BOT_PHRASES.get('recommend_main'), BOT_PHRASES.get('recommend_default')


class Chat:
    """This class contains the logic of communication with the user

            __init__
            :self._hlogic: (bool) True if say_hello, hello_null, hello_repeat
            :self._mlogic: (bool) True for all other logic
            :self._repeated: (bool) ask again a second time or hengup_null run
    """

    def __init__(self):
        self._hlogic = True
        self._mlogic = False
        self._repeated = False


    @staticmethod 
    def clean_data(response):
        return response.lower().strip()


    def say_hello(self, name):
        """<user name>, BOT_PHRASES['hello']"""
        hello = BOT_PHRASES["hello"]
        hello = self.format_text(hello)
        return time_input(hello.format(name))


    def format_text(self, phrase):
        """beep 🤖   >>  >>>    <bot phrase>"""
        return f'\n\a\N{Robot Face}\t>>\t>>>\t{phrase}\n\n'


    def check_repeat(self):
        """re-ask or hangup_null"""
        self._repeated = True if not self._repeated else False
        return self._repeated


    def check_pattern(self, response):
        """response in goto.keys()"""
        return any(list(filter(lambda x: x == response, list(goto.keys()))))


    def set_current_logic(self, is_pattern):
        """ :self._hlogic: (bool) True if say_hello, hello_null, hello_repeat
            :self._mlogic: (bool) True for all other logic
        """

        if is_pattern in ('нет', 'занят', 'еще раз'): return
        self._hlogic, self._mlogic = self._mlogic, self._hlogic


    def get_current_defаlt(self):
        """self._hlogic -> return recommend_main
           self._mlogic -> return recommend_default
        """
        return default[0 if self._hlogic else 1]


    def check_exit(self, response, key='foo'):
        """hangup logic"""
        return any(map(lambda w: w in goto['exit'], (key, response))) 


    def score_on_a_scale_of_1_to_10(self, n):
        """ rate: hangup_negative <- [0..8..10] -> hangup_positive"""
        good = goto.get('good')
        bad = goto.get('bad')

        return bad if int(n) in range(9) else good


    def trying_to_chat(self, response):
        """User is None:
                re-ask if not asked
                exit if it was
        
        """
        re_ask = self.check_repeat()

        if self._hlogic and re_ask:
            phrase = goto['null']['hello_null']
        elif not self._hlogic and re_ask:
            phrase = goto['null']['recommend_nul']
        elif not re_ask:
            phrase = goto['null']['hangup_null']
            raise sys.exit(self.format_text(phrase))
        return time_input(self.format_text(phrase))
    

    def chat_continue(self, response):
        """If user replied: goto: {response: function};
           if rated: exit; if null: re-ask
        
        """
        response = Bot.clean_data(response)
        is_pattern = self.check_pattern(response)

        try:
            if self._hlogic and is_pattern:
                key = list(goto.get(response).keys())[0]
                self.set_current_logic(response)

            elif self._mlogic and (is_pattern or response.isdigit()):
                
                if response.isdigit() and int(response) in range(11):
                        hungup = self.score_on_a_scale_of_1_to_10(response)
                        raise sys.exit(self.format_text(hungup))

                key = list(goto.get(response).keys())[1]

            default = self.get_current_defаlt()
            phrase = goto[response].get(key, default)

        except (KeyError, AttributeError):
            default = self.get_current_defаlt()
            phrase = goto.get(response, default)

        wrong_time = self.check_exit(response)
        if wrong_time: 
            raise sys.exit(self.format_text(phrase))

        return time_input(self.format_text(phrase))


class Bot(Chat):
    
    def say_hello(self, name):
        return super().say_hello(name.capitalize())


if __name__ == '__main__':
    bot = Bot('Chapa')


# при текущей "реализации", каждый раз при входных данных типа default,
# робот будет оставатся в петле hello_logic и возвращать recommend_main

# слишком раздутый event loop
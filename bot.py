import sys

from phrases import interaction
from utils import time_input


_, goto, default = interaction


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
        hello = interaction.bot_phrases.get('hello')
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

 
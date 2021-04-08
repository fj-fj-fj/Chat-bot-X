import sys

from INTERACTION import interaction
from utils import time_input

_, goto, default = interaction


class Chat:

    def __init__(self):
        self._hlogic = True
        self._mlogic = False
        self._repeated = False

    @staticmethod
    def clean_data(response):
        return response.lower().strip()

    def say_hello(self, name):
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
        if is_pattern in ('нет', 'занят', 'еще раз'): return  # noqa: E701
        self._hlogic, self._mlogic = self._mlogic, self._hlogic

    def get_current_defаlt(self):
        return default[0 if self._hlogic else 1]

    def check_exit(self, response, key='foo'):
        return any(map(lambda w: w in goto['exit'], (key, response)))

    def score_on_a_scale_of_1_to_10(self, n):
        good = goto.get('good')
        bad = goto.get('bad')
        return bad if int(n) in range(9) else good

    def trying_to_chat(self, response):
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

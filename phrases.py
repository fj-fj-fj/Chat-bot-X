import re
from collections import namedtuple


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



GOTO = {
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
DEFAULT = BOT_PHRASES.get('recommend_main'), BOT_PHRASES.get('recommend_default')


Interaction = namedtuple('Interaction', 'bot_phrases goto default')

Interaction.__doc__ += ': Interactions between machine and human'
Interaction.bot_phrases.__doc__ = 'Speech set for a robot'
Interaction.goto.__doc__ = 'User behavior patterns and bot reaction to them'
Interaction.default.__doc__ = 'Default behavior of the robot'

interaction = Interaction(BOT_PHRASES, GOTO, DEFAULT)


if __name__ == '__main__':
    
    for field in interaction._fields:
        doc = getattr(Interaction, field)
        print(f'Interaction.{field}.__doc__ : {doc.__doc__}')

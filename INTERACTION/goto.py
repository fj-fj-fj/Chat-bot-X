from enum import Enum

from .phrases import BOT_PHRASES

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
        'hangup_negative', 'занят',
    ],
}

# in: hey? out: [CROWLING AND SCREAMING]:
DEFAULT = BOT_PHRASES.get('recommend_main'), BOT_PHRASES.get('recommend_default')  # noqa: E501

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

Logic = Enum('Logic', 'HANGUP HELLO MAIN', start=0)

goto_alternative = {
    'null': {
        1: (BOT_PHRASES.get('hello_null'), Logic.HELLO.value),
        2: (BOT_PHRASES.get('recommend_null'), Logic.MAIN.value),
        None: (BOT_PHRASES.get('hangup_null'), Logic.HANGUP.value),
    },
    'да': {
        1: (BOT_PHRASES.get('recommend_main'), Logic.MAIN.value),
        2: (BOT_PHRASES.get('recommend_score_positive'), Logic.MAIN.value),
    },
    'нет': {
        1: (BOT_PHRASES.get('hangup_wrong_time'), Logic.HANGUP.value),
        2: (BOT_PHRASES.get('recommend_score_negative'), Logic.MAIN.value),
    },
    'занят': (BOT_PHRASES.get('hangup_wrong_time'), Logic.HANGUP.value),
    'не знаю': (BOT_PHRASES.get('recommend_repeat_2'), Logic.MAIN.value),
    'возможно': (BOT_PHRASES.get('recommend_score_neutral'), Logic.MAIN.value),
    'еще раз': {
        1: (BOT_PHRASES.get('hello_repeat'), Logic.HELLO.value),
        2: (BOT_PHRASES.get('recommend_repeat'), Logic.MAIN.value),
    },
    '?': (BOT_PHRASES.get('forward'), Logic.MAIN.value),  # nlu
    'bad': (BOT_PHRASES.get('hangup_negative'), Logic.HANGUP.value),
    'good': (BOT_PHRASES.get('hangup_positive'), Logic.HANGUP.value),
    'default': {
        1: (BOT_PHRASES.get('recommend_main'), Logic.MAIN.value),
        2: (BOT_PHRASES.get('recommend_default'), Logic.MAIN.value),
    }
}

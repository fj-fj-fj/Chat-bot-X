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
        'hangup_negative','занят',
    ]
}
# in: hey? out: [CROWLING AND SCREAMING]:
DEFAULT = BOT_PHRASES.get('recommend_main'), BOT_PHRASES.get('recommend_default')

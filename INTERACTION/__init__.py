from collections import namedtuple

from .goto import (  # noqa: F401
    GOTO, DEFAULT, BOT_PHRASES, Logic, goto_alternative as goto
)

Interaction = namedtuple('Interaction', 'bot_phrases goto default')

Interaction.__doc__ += ': Interactions between machine and human'
Interaction.bot_phrases.__doc__ = 'Speech set for a robot'
Interaction.goto.__doc__ = 'User behavior patterns and bot reaction to them'
Interaction.default.__doc__ = 'Default behavior of the robot'

interaction = Interaction(BOT_PHRASES, GOTO, DEFAULT)

from discussion_bot.bot import Bot
from discussion_bot.settings import TRAINING_DATA

_bot_instance = None

def get_bot_instance(filenames=set()):
    global _bot_instance
    if not _bot_instance:
        print 'initializing bot instance ...'
        if not filenames:
            filenames = {TRAINING_DATA}
        _bot_instance = Bot(filenames)
    return _bot_instance

def reply_to(text):
    return get_bot_instance().reply(text)

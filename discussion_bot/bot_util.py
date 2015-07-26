import os
from discussion_bot.bot import Bot
from discussion_bot.settings import APP_ROOT

_bot_instance = None

def get_bot_instance(filenames=set()):
    global _bot_instance
    if not _bot_instance:
        print 'initializing bot instance ...'
        if not filenames:
            training_data_dir = os.path.join(APP_ROOT, 'bot_data/train')
            filenames = [os.path.join(dp, f) for dp, dn, filenames in os.walk(training_data_dir)
                         for f in filenames if os.path.splitext(f)[1] == '.txt']
            print filenames
        _bot_instance = Bot(filenames)
    return _bot_instance

def reply_to(text):
    return get_bot_instance().reply(text)

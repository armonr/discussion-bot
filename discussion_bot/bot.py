import os
import cobe.brain
from discussion_bot.settings import APP_ROOT


class Bot:
    bot_brain = None
    brain_file = os.path.join(APP_ROOT, 'bot_data/cobe.brain')

    def __init__(self, filenames=set()):
        self.bot_brain = cobe.brain.Brain(self.brain_file)
        self._cobe_batch_learning(filenames)

    def _cobe_batch_learning(self, filenames=set()):
        self.bot_brain.start_batch_learning()
        for filename in filenames:
            count = 0
            with open(filename, 'r') as fd:
                for line in fd:
                    self.bot_brain.learn(line.strip())
                    count += 1
                    if count % 10000 == 0:
                        self.bot_brain.graph.commit()
        self.bot_brain.stop_batch_learning()

    def reply(self, text):
        if not text:
            raise Exception("no text provided!")
        return self.bot_brain.reply(text).encode("utf-8")

#!/usr/bin/env python

import unittest
from flaky import flaky

from source.services.handler import Handler

from tests.mocks.bot import Bot
from tests.mocks.update import Update

@flaky
class HandlerTest(unittest.TestCase):

    def test_start(self):
        bot = Bot()
        update = Update()
        Handler.start(bot, update)
        assert bot.text is not None
        assert bot.chat_id is 'chat_id'

    def test_greet(self):
        bot = Bot()
        update = Update()
        Handler.greet(bot, update)
        assert bot.text is not None
        assert bot.chat_id is 'chat_id'

    def test_about(self):
        bot = Bot()
        update = Update()
        Handler.about(bot, update)
        assert bot.text is not None
        assert bot.chat_id is 'chat_id'

if __name__ == "__main__":
    unittest.main()

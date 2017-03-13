from .info import Info

class Handler:

    @staticmethod
    def start(bot, update):
        bot.sendMessage(update.message.chat_id, text = Info.start())

    @staticmethod
    def greet(bot, update):
        bot.sendMessage(update.message.chat_id, text = 'Hi!')

    @staticmethod
    def about(bot, update):
        bot.sendMessage(update.message.chat_id, text = Info.about())

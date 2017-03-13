#!/usr/bin/env python

from services.handler import Handler
from utils.token import TOKEN
from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", Handler.start))
    dispatcher.add_handler(CommandHandler("greet", Handler.greet))
    dispatcher.add_handler(CommandHandler("about", Handler.about))

    updater.start_polling()

    print("Initialized")
    updater.idle()

if __name__ == "__main__":
    main()

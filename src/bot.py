import telebot
import os
from loguru import logger


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['anonntelegram_bot_TOKEN'])
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)

    def run(self):
        logger.info('Bot is running ...')
        self.bot.infinity_polling()

    def echo_all(self, message):
        self.bot.reply_to(message, message.text)

if __name__ == '__main__':
    logger.info('Bot started!')
    bot = Bot()
    bot.run()


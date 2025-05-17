import telebot
from telebot import TeleBot

from src.keyboards import all_buttons
from settings import settings
from src.actions import get_action
from src.logger import logger


def create_bot() -> TeleBot:
    telegram_bot: TeleBot = telebot.TeleBot(settings.token, parse_mode="HTML")

    @telegram_bot.message_handler(commands=['ping'])
    def ping(message):
        bot.send_message(message.chat.id, "pong")
        logger.info('Проверка работоспособности')

    @telegram_bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            "Добро пожаловать в игру БУНКЕР!\nВыберите одно из действий:",
            reply_markup=all_buttons,
        )
        logger.info('Подключен новый пользователь')

    @telegram_bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        action = get_action(call)
        action(bot, call)

    return telegram_bot


bot = create_bot()

from telebot import TeleBot, types

from data.keyboards import all_buttons
from src.message import SituationMessageCreator, CharacteristicMessageCreator
from src.logger import logger


def create_situation(bot: TeleBot, call: types.CallbackQuery):
    msg = SituationMessageCreator.get_message()
    bot.send_message(
        call.message.chat.id,
        msg,
        reply_markup=all_buttons,
    )
    logger.info('Отправлена ситуация')


def get_characteristic(bot: TeleBot, call: types.CallbackQuery):
    msg = CharacteristicMessageCreator.get_message()
    bot.send_message(
        call.message.chat.id,
        msg,
        reply_markup=all_buttons,
    )
    logger.info('Отправлена характеристика')


def warning_unknown_command(bot: TeleBot, call: types.CallbackQuery):
    msg = "Неизвестная команда, выберите одну из доступных:"
    bot.send_message(
        call.message.chat.id,
        msg,
        reply_markup=all_buttons,
    )
    logger.warning(f'Неизвестная команда "{call.data}"')


def get_action(call: types.CallbackQuery):
    call_mapping = {
        'create_situation': create_situation,
        'get_characteristic': get_characteristic,
    }
    return call_mapping.get(call.data, warning_unknown_command)

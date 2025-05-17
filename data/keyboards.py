import telebot

# Кнопка "Ситуация"
button_situation = telebot.types.InlineKeyboardButton(
    "Ситуация",
    callback_data="create_situation",
)

# Кнопка "Характеристика"
button_characteristic = telebot.types.InlineKeyboardButton(
    "Характеристика",
    callback_data="get_characteristic",
)


def merge_buttons(*buttons):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


all_buttons = merge_buttons(
    button_situation,
    button_characteristic,
)

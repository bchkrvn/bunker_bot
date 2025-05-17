from src.bot import bot
from logger import logger

logger.info('Бот запущен')
bot.infinity_polling()

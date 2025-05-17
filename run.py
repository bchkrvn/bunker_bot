from src.bot import bot
from src.logger import logger

logger.info('Бот запущен')
bot.infinity_polling()

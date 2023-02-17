from aiogram import executor

from bot.handlers import register
from config.config import DISP
from config.log_config import Logger as Log


def bot_starter():
    Log.logger.info('[BOT] Bot has been started')
    register.start_handler(DISP)
    register.return_to_menu_handler(DISP)
    register.about_handler(DISP)
    register.faq_handler(DISP)
    register.support_dev_handler(DISP)
    register.usr_ads_handler(DISP)
    executor.start_polling(DISP, skip_updates=True)

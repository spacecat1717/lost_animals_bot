from aiogram import Dispatcher

from bot.handlers import main_menu
from config.config import DISP


def start_handler(dp: Dispatcher):
    DISP.register_message_handler(main_menu.start, commands='start')

from aiogram import Dispatcher

from bot.handlers import main_menu, info_handlers
from config.config import DISP


def start_handler(dp: Dispatcher):
    DISP.register_message_handler(main_menu.start, commands='start')


def return_to_menu_handler(dp: Dispatcher):
    DISP.register_message_handler(main_menu.return_to_main_menu)


def about_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.about)


def faq_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.faq)


def support_dev_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.support_dev)


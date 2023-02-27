from aiogram import Dispatcher

from bot.handlers.base_handlers import info_handlers, main_menu
from bot.handlers.ad_handlers import user_ads_handlers
from config.config import DISP


def start_handler(dp: Dispatcher):
    DISP.register_message_handler(main_menu.start, commands='start')


def return_to_menu_handler(dp: Dispatcher):
    DISP.register_message_handler(main_menu.return_to_main_menu)


def about_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.about)


def faq_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.faq)


def donate_dev_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.donate_dev)


def usr_ads_handler(dp: Dispatcher):
    DISP.register_message_handler(user_ads_handlers.usr_ads_list)


def support_msg_handler(dp: Dispatcher):
    DISP.register_message_handler(info_handlers.support_msg)
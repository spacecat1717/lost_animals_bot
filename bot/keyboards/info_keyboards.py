from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.main_menu_keyboard import MENU_KEY


def kb_about():
    about_kb = InlineKeyboardMarkup()
    support = InlineKeyboardButton(text='Поддержать разработчика', callback_data='support_dev')
    about_kb.row(support)
    about_kb.row(MENU_KEY)
    return about_kb




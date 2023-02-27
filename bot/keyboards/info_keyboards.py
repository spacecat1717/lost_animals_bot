from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.const_keys import MENU_KEY, SUPPORT_KEY


def kb_about():
    about_kb = InlineKeyboardMarkup()
    donate = InlineKeyboardButton(text='Поддержать разработчика', callback_data='donate_dev')
    about_kb.row(donate)
    about_kb.row(SUPPORT_KEY)
    about_kb.row(MENU_KEY)
    return about_kb




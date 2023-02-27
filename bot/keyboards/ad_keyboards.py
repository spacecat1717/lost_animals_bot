from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.main_menu_keyboard import MENU_KEY


def usr_ad_kb():
    ad_kb = InlineKeyboardMarkup()
    close = InlineKeyboardButton(text='Закрыть объявление', callback_data='close_ad')
    ad_kb.row(close)
    ad_kb.row(MENU_KEY)
    return ad_kb


def create_ad_kb():
    kb = InlineKeyboardMarkup()
    create = InlineKeyboardButton(text='Создать объявление', callback_data='create_ad')
    kb.add(create)
    return kb

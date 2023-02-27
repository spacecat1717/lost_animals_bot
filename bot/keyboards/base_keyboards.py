"""There are keyboards for navigation"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.const_keys import MENU_KEY, SUPPORT_KEY


def kb_return_to_menu():
    back_kb = InlineKeyboardMarkup()
    back_kb.add(MENU_KEY)
    return back_kb


def kb_support():
    support_kb = InlineKeyboardMarkup()
    support_kb.add(SUPPORT_KEY)
    return support_kb

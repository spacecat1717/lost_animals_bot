"""There are the keys those are the most usable"""

from aiogram.types import InlineKeyboardButton

MENU_KEY = InlineKeyboardButton(text='Вернуться в меню', callback_data='main_menu')

SUPPORT_KEY = InlineKeyboardButton(text='Сообщить об ошибке', callback_data='support_msg')

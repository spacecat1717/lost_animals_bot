from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_about():
    about_kb = InlineKeyboardMarkup()
    support = InlineKeyboardButton(text='Поддержать разработчика', callback_data='support_dev')
    main_menu = InlineKeyboardButton(text='Вернуться в меню', callback_data='main_menu')
    about_kb.row(support)
    about_kb.row(main_menu)
    return about_kb




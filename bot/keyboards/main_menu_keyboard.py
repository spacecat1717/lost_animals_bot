from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_main_menu():
    main_kb = InlineKeyboardMarkup()
    about = InlineKeyboardButton(text='О проекте', callback_data='about')
    faq = InlineKeyboardButton(text='FAQ', callback_data='faq')
    my_ads = InlineKeyboardButton(text='Мои объявления', callback_data='my_ads')
    found = InlineKeyboardButton(text='Я нашел питомца', callback_data='found_start')
    lost = InlineKeyboardButton(text='Я потерял питомца', callback_data='lost_start')
    all_lost = InlineKeyboardButton(text='Потерялись', callback_data='all_lost')
    all_found = InlineKeyboardButton(text='Найдены', callback_data='all_found')
    main_kb.row(about, faq)
    main_kb.row(my_ads)
    main_kb.row(found, lost)
    main_kb.row(all_lost, all_found)
    return main_kb


def kb_return_to_menu():
    back_kb = InlineKeyboardMarkup()
    main_menu = InlineKeyboardButton(text='Вернуться в меню', callback_data='main_menu')
    back_kb.add(main_menu)
    return back_kb

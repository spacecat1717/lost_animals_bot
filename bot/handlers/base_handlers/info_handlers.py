from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from bot.keyboards.info_keyboards import kb_about
from bot.keyboards.main_menu_keyboard import kb_return_to_menu
from config.config import BOT, DISP
from config.log_config import Logger as Log

#remove in production
DISP.middleware.setup(LoggingMiddleware())


#TODO: add correct text into about, faq and support_dev


@DISP.callback_query_handler(lambda c: c.data == 'about')
async def about(callback: types.CallbackQuery):
    await callback.message.answer(text="It'll be the description of the project", reply_markup=kb_about())


@DISP.callback_query_handler(lambda c: c.data == 'faq')
async def faq(callback: types.CallbackQuery):
    await callback.message.answer(text="It'll be the FAQ", reply_markup=kb_return_to_menu())


@DISP.callback_query_handler(lambda c: c.data == 'support_dev')
async def support_dev(callback: types.CallbackQuery):
    await callback.message.answer(text="It'll be an info how to support me lol", reply_markup=kb_return_to_menu())




from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from bot.keyboards.main_menu_keyboard import kb_main_menu
from config.config import BOT, DISP
from config.log_config import Logger as Log


DISP.middleware.setup(LoggingMiddleware())

async def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    Log.logger.info('[BOT] User %r is using the bot', user_id)
    await message.answer(f'Добро пожаловать, {username}!', reply_markup=kb_main_menu())

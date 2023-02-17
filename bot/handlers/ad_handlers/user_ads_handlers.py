from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text, bold

from bot.states.ad_states.close_ad_states import CloseAdState
from bot.keyboards.ad_keyboards import usr_ad_kb
from config.config import BOT, DISP
from config.log_config import Logger as Log
from database.ads.ad_manager import AdManager


#remove in production
DISP.middleware.setup(LoggingMiddleware())


@DISP.callback_query_handler(lambda c: c.data == 'my_ads')
async def usr_ads_list(callback: types.CallbackQuery):
    manager = AdManager()
    usr_id = callback.from_user.id
    ad_list = await manager.get_user_ads(int(usr_id))
    if ad_list:
        for ad in ad_list:
            msg_text = text(
                bold('Тип объявления:'), f' {ad.type}\n',
                bold('Город:'), f' {ad.city}\n',
                bold('Район:'), f' {ad.district}\n',
                bold('Дата создания:'), f' {ad.creation_date}\n',
                bold('Вид питомца:'), f' {ad.species}\n',
                bold('Кличка:'), f' {ad.name}\n',
                bold('Описание:'), f' {ad.description}\n',
                bold('Чип:'), ' Да' if ad.chip else ' Нет',
            )
            #msg_text = (
            #    f'Тип объявления: {ad.type}\n'
            #    f'Город: {ad.city}\n'
            #    f'Район: {ad.district}\n'
            #    f'Дата создания: {ad.creation_date}\n'
            #    f'Вид питомца: {ad.species}\n'
            #    f'Кличка: {ad.name}\n'
            #    f'Описание: {ad.description}\n'
            #    f'Чип: {ad.chip}\n'
            #)
            await callback.message.answer(msg_text, reply_markup=usr_ad_kb())
            #await callback.message.answer_photo(open(f'{ad.photo1}', 'r'), msg_text, reply_markup=usr_ad_kb())



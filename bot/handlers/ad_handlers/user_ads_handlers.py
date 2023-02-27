import aiogram.utils.exceptions
from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text, bold

from bot.states.ad_states.close_ad_states import CloseAdState
from bot.keyboards.ad_keyboards import usr_ad_kb, create_ad_kb
from bot.keyboards.base_keyboards import kb_support
from bot.utils.photo_optimizer import resize
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
            pic = types.InputFile(ad.photo)
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
            try:
                await callback.message.answer_photo(photo=pic, caption=msg_text, reply_markup=usr_ad_kb())
            except aiogram.utils.exceptions.PhotoDimensions as e:
                msg_text = text(
                        emojize('Я не могу загрузить объявление :crying face:'),
                        'Пожалуйста, обратитесь к разработчику или попробуйте позже\n'
                    )
                await callback.message.answer(msg_text, reply_markup=kb_support())
                Log.logger.error('[BOT] ERROR: %r', e)
        Log.logger.info('[BOT] User %r uploaded his ads', usr_id)
    #else:
    #    Log.logger.info('[BOT] User %r uploaded his ads, but there is nothing', usr_id)
    #    msg_text = text('Вы еще не создали ни одного объявления')
    #    await callback.message.answer(msg_text, reply_markup=create_ad_kb())





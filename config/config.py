import os

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()

"""DB settings"""
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

"""TLG settings"""
TLG_TOKEN = os.getenv('TLG_TOKEN')
TLG_OWNER = os.getenv('TLG_OWNER')
BOT = Bot(token=TLG_TOKEN)
DISP = Dispatcher(BOT, storage=MemoryStorage())

"""Const"""
#species list for ads' creation
SPECIES = ['Кошка', 'Собака', 'Другое']
#reasons lists for ads' closing
REASONS_LOST = ['Нашли сами', 'Нашли через бота', 'Нашли через волонтеров/другой проект']
REASONS_FOUND = ['Нашли через бота', 'Нашли через волонтеров/другие проекты', 'Оставили себе']






# from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.contrib.fsm_storage.redis import RedisStorage2

bot = Bot(token='6874803413:AAEZBIpD2PGpF32j5pSnEzeFHJXVGiUC5eU', parse_mode=types.ParseMode.HTML)
#storage = RedisStorage2(port=7777)
dp = Dispatcher(bot, storage=MemoryStorage())

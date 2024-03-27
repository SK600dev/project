import handlers
from aiogram import executor

from loader import dp
# TODO сделать списки задач, выгрузку на сегодня, завтра, по задачам

# TODO сделать уведомления по задачам
# TODO при добавлении задачи можно сделать парсинг названия, например @список в который добавить,
#  # какой-то тег

if __name__ == '__main__':
    executor.start_polling(dp)

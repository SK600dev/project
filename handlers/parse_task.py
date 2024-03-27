from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import keybords
from loader import dp
from models.parse_date import parse_date
from states import AddTask
from utils import db, set_new_at_job


@dp.message_handler(commands='add')
async def add_task(message: types.Message):
    await message.answer('Введите название задачи:\n')

    await AddTask.AddName.set()


@dp.message_handler(state=AddTask.AddName)
async def add_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer("Введите дату выполнения задачи в формате dd mm yy",
                         reply_markup=keybords.add_date_in_task)
    await AddTask.AddDate.set()


@dp.message_handler(state=AddTask.AddDate)
async def add_date_from_text(message: types.Message, state: FSMContext):
    answer = message.text
    try:
        if answer.isalpha():
            answer = parse_date(answer)
            date = datetime.strptime(answer.strip(), "%d %m %y")
        else:
            date = datetime.strptime(answer.strip(), "%d %m %y")
            if date.date() < datetime.today().date():
                await message.answer("Дата меньше текущей")
                raise ValueError('Дата меньше текущей')
    except ValueError:
        await message.answer("Попробуйте ещё раз.\nВведите дату"
                             " выполнения задачи в формате dd mm yy")
        return

    await state.update_data(date=date.strftime("%y %m %d"))
    await message.answer("Добавьте текстовое описание задачи: ",
                         reply_markup=keybords.description)
    await AddTask.AddDescription.set()


@dp.callback_query_handler(keybords.add_date_callback.filter(), state=AddTask.AddDate)
async def add_date(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    call.message.text = callback_data.get('date')
    await add_date_from_text(call.message, state)


@dp.callback_query_handler(keybords.inline_data_callback.add_description_callback.filter(description='false'),
                           state=AddTask.AddDescription)
async def skip_description(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    data = await state.get_data()
    name = data.get('name')
    date = data.get('date')
    db.add_task(call.from_user.id, name, date, ' ')
    await call.message.answer('Вы успешно добавили задачу!\n'
                              f'Название : {name}\n'
                              f'Выполнить до : {" ".join(date.split()[::-1]).replace(" ", "/")}\n')
    await call.message.answer("Если хотите добавить уведомление напишите время в формате HH:MM: ",
                              reply_markup=keybords.cancel)
    await AddTask.AddNotification.set()


@dp.message_handler(state=AddTask.AddDescription)
async def add_description(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(description=answer)
    data = await state.get_data()
    name = data.get('name')
    date = data.get('date')
    description = data.get('description')
    db.add_task(message.from_user.id, name, date, description)
    await message.answer('Вы успешно добавили задачу!\n'
                         f'Название : {name}\n'
                         f'Выполнить до : {" ".join(date.split()[::-1]).replace(" ", "/")}\n'
                         f'Описание : {description}')
    await AddTask.AddNotification.set()
    await message.answer("Если хотите добавить уведомление напишите время в формате HH:MM: ",
                         reply_markup=keybords.cancel)


@dp.callback_query_handler(keybords.keybords.edit_task_callback.filter(action='cancel'),
                           state=AddTask)
async def stop_add_tasks(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.reset_state()


@dp.message_handler(state=AddTask.AddNotification)  # добавляем уведомление
async def add_notification(message: types.Message, state: FSMContext):
    time_ = message.text
    try:
        datetime.strptime(time_, "%H:%M")
    except ValueError:
        await message.answer('Время должно быть в формате HH:MM: ',
                             reply_markup=keybords.cancel)
        return
    data = await state.get_data()
    date_ = data.get('date').split()[::-1]
    date_at = f"{time_} {date_[0]}.{date_[1]}.20{date_[2]}"
    name = data.get('name')
    description = data.get('description')
    text = 'Напоминаю!\n' \
           f'Название : {name}\n' \
           f'Выполнить до : {" ".join(date_).replace(" ", "/")}\n' \
           f'Описание : {description}'

    set_new_at_job(message.from_user.id, date_at, text)

    await state.reset_state()

from aiogram.dispatcher.filters.state import StatesGroup, State


class GetTask(StatesGroup):
    GetTasks = State()
    ViewTask = State()
    DoneTask = State()
    EditName = State()
    EditDate = State()
    EditDescription = State()

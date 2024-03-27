from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keybords.inline_data_callback import add_date_callback, add_description_callback
from keybords.inline_data_callback.callback_data import edit_task_callback

add_date_in_task = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text='Сегодня',
                                                    callback_data=add_date_callback.new(date='today')
                                                ),
                                                InlineKeyboardButton(
                                                    text='Завтра',
                                                    callback_data=add_date_callback.new(date='tomorrow')
                                                ),
                                                InlineKeyboardButton(
                                                    text='Через неделю',
                                                    callback_data=add_date_callback.new(date='week')
                                                )
                                            ]
                                        ])

get_tasks = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text='Сегодня',
                                             callback_data='сегодня'
                                         ),
                                         InlineKeyboardButton(
                                             text='Завтра',
                                             callback_data='завтра'
                                         ),
                                         InlineKeyboardButton(
                                             text='Все',
                                             callback_data='все'
                                         )
                                     ]
                                 ])

description = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text='Не добавлять описание',
                                               callback_data=add_description_callback.new(description='false')
                                           )
                                       ]
                                   ])

action_tasks = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text='Выполнить задачу',
                                                callback_data=edit_task_callback.new(action='done')
                                            ),
                                            InlineKeyboardButton(
                                                text='Назад',
                                                callback_data=edit_task_callback.new(action='back')
                                            ),
                                            InlineKeyboardButton(
                                                text='Редактировать задачу',
                                                callback_data=edit_task_callback.new(action='edit')
                                            )
                                        ]
                                    ])

action_back = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text='Назад',
                                               callback_data=edit_task_callback.new(action='back')
                                           ),
                                           InlineKeyboardButton(
                                               text='Выйти',
                                               callback_data=edit_task_callback.new(action='cancel')
                                           )
                                       ]
                                   ])

edit_task = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text='Название',
                                             callback_data=edit_task_callback.new(action='name')
                                         ),
                                         InlineKeyboardButton(
                                             text='Дата',
                                             callback_data=edit_task_callback.new(action='date')
                                         ),
                                         InlineKeyboardButton(
                                             text='Описание',
                                             callback_data=edit_task_callback.new(action='description')
                                         )
                                     ]
                                 ])

cancel = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='Отмена',
                                          callback_data=edit_task_callback.new(action='cancel')
                                      )
                                  ]

                              ])

from datetime import datetime


class Description:
    def __init__(self, text, media=None):
        self.media = media
        self.text = text


class Task:
    def __init__(self, id: int, id_user: int, name: str, date: str, description_id: int):
        self.description_id: int = description_id
        self.date: datetime = datetime.strptime(date, '%y %m %d')
        self.name: str = name
        self.id_user: int = id_user
        self.id: int = id

    def return_data(self):
        return self.id, self.id_user, self.name, self.date.strftime('%y %m %d'), self.description_id

    def __str__(self):
        days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс', ]
        return f'{self.name} {days[self.date.weekday()]} ({self.date.strftime("%d/%m/%y")})'

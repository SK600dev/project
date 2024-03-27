from datetime import datetime, timedelta


def parse_date(message: str):
    # TODO Пофиксить дни недели
    d = datetime.today().date()
    weekdays = {'Пн': 0,
                'Вт': 1,
                'Ср': 2,
                'Чт': 3,
                'Пт': 4,
                'Сб': 5,
                'Вс': 6,
                }
    if message == 'today':
        return d.strftime('%d %m %y')
    if message == 'tomorrow':
        d += timedelta(days=1)
        return d.strftime('%d %m %y')
    if message == 'week':
        d += timedelta(days=7)
        return d.strftime('%d %m %y')
    # if message in weekdays.keys():
    #     d += timedelta(days=abs(d.weekday() - weekdays[message]))
    #     return d.strftime('%d %m %y')
    raise ValueError('Неизвестное сокращение')


import tempfile
import os

def set_new_at_job(chat_id, time, text):
    """
    Sets a new task in Windows Task Scheduler
    :param chat_id: User's chat_id
    :param time: time in HH:MM format
    :param text: text to send to user
    :return: task name / None if error occurred
    """
    tmp = tempfile.NamedTemporaryFile(mode='r+t', delete=False)
    tmp_file_path = tmp.name
    tmp.close()

    command = 'schtasks /create /sc once /st {0} /tn MyTask /tr "python C:\\PROJECT_BOT\\utils\\sender.py {1} \'{2}\'"'.format(time, chat_id, text)
    print(command)

    os.system(command)

    os.remove(tmp_file_path)  # Удаляем временный файл

    return 'MyTask'  # Возвращаем имя задачи, можно изменить на более подходящее
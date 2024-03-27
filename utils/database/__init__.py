from sqlite3 import OperationalError

from .database_task import DatabaseTasks

db = DatabaseTasks()
try:
    db.create_db()
except OperationalError:
    pass

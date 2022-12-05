# https://github.com/coleifer/peewee

from peewee import *
import datetime

from .entities.user import User

def db_init():
    
    db = SqliteDatabase('db.db')

    db.connect()
    try:
        db.create_tables([User])
        User.create(username="admin")
    except Exception as e:
        pass

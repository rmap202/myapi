# https://github.com/coleifer/peewee

from peewee import *
import datetime

from .entities.user import User

def db_init():
    
    db = SqliteDatabase('db.db')

    db.connect()
    db.create_tables([User])

    admin = User.create(username="admin")

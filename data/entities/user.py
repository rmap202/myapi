from peewee import *

from .base import BaseModel

class User(BaseModel):
    username = CharField(unique=True)

import jwt

from peewee import *

from data.entities.user import User
from domain.models.response import ResponseModel
from domain.models.user import UserModel

# TODO: Move to .env
my_secret = 'my_super_secret'


def create_jwt_token(payload_data) -> str:
    token = jwt.encode(
        payload = payload_data,
        key = my_secret
    )
    return token

def register(user : UserModel) -> bool:
    # check if user model is valid
    
    # check if user in db  
    is_user = User.select().where(User.username == user.username)  
    if (is_user):
        return False
    
    # create new user
    db = SqliteDatabase('db.db')
    db.connect()
    User.create(username = user.username)

    
    # create jwt
    
    # send back jwt
    return True
    

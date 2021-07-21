from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import jwt
from bson.objectid import ObjectId
import backend.services.users as userService
import backend.services.admins as adminService


def login(email, password):
    users = mongo.db.users
    login_user = users.find_one({'email': email})
    if login_user:
        return userService.login(login_user, email, password)
    else:
        admins = mongo.db.admins
        login_admin = admins.find_one({'email': email})
        if login_admin:
            return adminService.login(login_admin, email, password)

    raise Exception('Invalid username/password combination')


def generate_token(user_id):
    try:
        payload = {
            'id': str(user_id)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    except Exception as e:
        return e

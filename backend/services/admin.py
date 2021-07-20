from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import jwt
from bson.objectid import ObjectId

# print(mongo)


def add(email, password):
    admins = mongo.db.admins
    newAdmin = {'email': email}
    existing_admin = admins.find_one({'email': email})

    if existing_admin is not None:
        return existing_admin

    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    newAdmin['password'] = hashpass.decode('utf-8')

    admins.insert(newAdmin)

    return newAdmin

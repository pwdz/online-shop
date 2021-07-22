from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import backend.utils.login as loginService
import jwt
from bson.objectid import ObjectId

# print(mongo)


def add(email, password):
    admins = mongo.db.admins
    new_admin = {'email': email}
    existing_admin = admins.find_one({'email': email})

    if existing_admin is not None:
        return existing_admin

    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_admin['password'] = hashpass.decode('utf-8')

    admins.insert(new_admin)

    return new_admin


def login(login_admin, email, password):
    admins = mongo.db.admins
    if bcrypt.hashpw(password.encode('utf-8'), login_admin['password'].encode('utf-8')) == login_admin['password'].encode('utf-8'):
        token = loginService.generate_token(login_admin['_id'])
        login_admin['token'] = token.decode(encoding="utf-8")
        admins.save(login_admin)
        return {'email': email, 'name': 'ادمین', 'token': login_admin['token']}
    else:
        raise Exception('Invalid credentials')


def check_token(token):
    admins = mongo.db.admins
    valid = True
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    if not payload['id']:
        valid = False
    user = admins.find_one({'_id': ObjectId(payload['id'])})
    print(payload['id'])
    if not user:
        valid = False

    return valid

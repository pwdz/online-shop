from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import jwt
from bson.objectid import ObjectId
import backend.utils.login as loginService

# print(mongo)


def register(email, password, name=None, lastname=None, address=None):
    users = mongo.db.users
    new_user = {'email': email, 'balance': 0}
    existing_user = users.find_one({'email': email})

    if existing_user is not None:
        raise Exception('That username already exists!')

    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user['password'] = hashpass.decode('utf-8')
    if name:
        new_user['name'] = name
    if lastname:
        new_user['lastname'] = lastname
    if address:
        new_user['address'] = address

    users.insert(new_user)
    new_user['_id'] = str(new_user['_id'])
    return new_user


def increase_balance(me, balance=0):
    users = mongo.db.users
    user = users.find_one({'token': me})
    user["balance"] += int(balance)
    users.save(user)
    user['_id'] = str(user['_id'])
    return user


def decrease_balance(me, balance=0):
    users = mongo.db.users
    user = users.find_one({'token': me})
    user["balance"] -= int(balance)
    users.save(user)
    user['_id'] = str(user['_id'])
    return user

# def get_user(user_id):
#     users = mongo.db.users
#     user = users.find_one({'_id': ObjectId(user_id)})
#     if user is None:
#         raise Exception('User is not found')

#     return {'name': user['name', 'lastname': user['lastname'], 'address': user['address']]}


def edit(me, password=None, name=None, lastname=None, address=None):
    users = mongo.db.users
    user = users.find_one({'token': me})

    if user is None:
        raise Exception('User is not found!')
    if password:
        hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user['password'] = hashpass.decode('utf-8')
    if name:
        user['name'] = name
    if lastname:
        user['lastname'] = lastname
    if address:
        user['address'] = address

    users.save(user)
    user['_id'] = str(user['_id'])
    return user


def login(login_user, email, password):
    users = mongo.db.users
    if bcrypt.hashpw(password.encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
        token = loginService.generate_token(login_user['_id'])
        login_user['token'] = token.decode(encoding="utf-8")
        users.save(login_user)
        return {'email': email, 'token': login_user['token']}
    else:
        raise Exception('Invalid credentials')


def check_token(token):
    users = mongo.db.users
    valid = True
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    if not payload['id']:
        valid = False
    user = users.find_one({'_id': ObjectId(payload['id'])})
    print(payload['id'])
    if not user:
        valid = False

    return valid

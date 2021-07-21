from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import jwt
from bson.objectid import ObjectId

# print(mongo)


def register(email, password, name=None, lastname=None, address=None):
    users = mongo.db.users
    newUser = {'email': email, 'balance': 0}
    existing_user = users.find_one({'email': email})

    if existing_user is not None:
        raise Exception('That username already exists!')

    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    newUser['password'] = hashpass.decode('utf-8')
    if name:
        newUser['name'] = name
    if lastname:
        newUser['lastname'] = lastname
    if address:
        newUser['address'] = address

    users.insert(newUser)

    return newUser


def increase_balance(me, balance):
    users = mongo.db.users
    user = users.find_one({'token': me})
    user["balance"] = balance
    users.save(user)

    return user


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

    return user


def login(email, password):
    users = mongo.db.users
    login_user = users.find_one({'email': email})

    if login_user:
        if bcrypt.hashpw(password.encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            token = generate_token(login_user['_id'])
            login_user['token'] = token.decode(encoding="utf-8")
            users.save(login_user)
            return {'email': email, 'token': login_user['token']}

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

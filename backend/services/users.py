from backend.extensions import mongo
import bcrypt
from uuid import uuid4

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

    return True


def login(email, password):
    users = mongo.db.users
    login_user = users.find_one({'email': email})

    if login_user:
        if bcrypt.hashpw(password.encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            token = uuid4()
            login_user['token'] = str(token)
            users.save(login_user)
            return {'email': email, 'token': token}

    raise Exception('Invalid username/password combination')

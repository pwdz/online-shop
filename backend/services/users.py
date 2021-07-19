from backend.extensions import mongo
import bcrypt


def register(email, password, name=None, lastname=None, address=None):
    users = mongo.db.users
    newUser = {'email': email, 'balance': 0}
    existing_user = users.find_one({})

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

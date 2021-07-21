from backend.extensions import mongo
from bson.objectid import ObjectId
from datetime import datetime

# print(mongo)


def add(product_name, number_of_products, me, price):
    receipts = mongo.db.receipts
    users = mongo.db.users
    user = users.find_one({'token': me})
    name = ''
    lastname = ''
    address = ''
    if user['name']:
        name = user['name']
    if user['lastname']:
        lastname = user['lastname']
    if user['address']:
        address = user['address']
    new_receipt = {'product': product_name, 'number': number_of_products,
                   'user': ObjectId(user['_id']), 'name': name, 'lastname': lastname, 'address': address, 'price': price, 'date': datetime.now()}

    receipts.insert(new_receipt)
    new_receipt['_id'] = str(new_receipt['_id'])
    new_receipt['user'] = str(new_receipt['user'])
    return new_receipt


def get_list(me=None):
    receipts = mongo.db.receipts
    records = []
    output = []

    if me:
        users = mongo.db.users
        user = users.find_one({'token': me})
        records = receipts.find({ObjectId(user['_id'])})
        for record in records:
            record['_id'] = str(record['_id'])
        output.append(record)
    else:
        records = receipts.find()
        for record in records:
            record['_id'] = str(record['_id'])
        output.append(record)
    return output

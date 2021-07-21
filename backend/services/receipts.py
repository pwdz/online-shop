from backend.extensions import mongo
from bson.objectid import ObjectId
from datetime import datetime
import random
import string
# seed random number generator


# print(mongo)


def add(product_name, number_of_products, me, price, state='processing'):
    receipts = mongo.db.receipts
    users = mongo.db.users
    user = users.find_one({'token': me})
    name = ''
    lastname = ''
    address = ''

    if 'name' in user:
        name = user['name']
    if 'lastname' in user:
        lastname = user['lastname']
    if 'address' in user:
        address = user['address']

    tracking = ''.join((random.choice(string.ascii_lowercase)
                        for x in range(10)))

    print(tracking)
    new_receipt = {'product': product_name, 'number': number_of_products,
                   'user': ObjectId(user['_id']), 'name': name, 'lastname': lastname, 'tracking': tracking, 'address': address, 'price': price, 'date': datetime.now(), 'state': state}

    receipts.insert(new_receipt)
    new_receipt['_id'] = str(new_receipt['_id'])
    new_receipt['user'] = str(new_receipt['user'])
    return new_receipt


def get_list(me=None, tracking=None):
    receipts = mongo.db.receipts
    records = []
    output = []

    if me:

        users = mongo.db.users
        user = users.find_one({'token': me})
        records = receipts.find({'user': ObjectId(user['_id'])})
        for record in records:
            record['_id'] = str(record['_id'])
            output.append({'_id': record['_id'], 'product': record['product'], 'number': record['number'],
                           'address': record['address'], 'price': record['price'], 'date': record['date'], 'state': record['state']})

    else:
        if tracking:
            records = receipts.find({'tracking': tracking})
        else:
            records = receipts.find()
        for record in records:
            record['_id'] = str(record['_id'])
            record['user'] = str(record['user'])
            output.append(record)

    return output


def change_state(receipt_id, state):
    receipts = mongo.db.receipts
    receipt = receipts.find_one({'_id': ObjectId(receipt_id)})

    if receipt is None:
        raise Exception('Receipt is not found')

    receipt['state'] = state

    receipts.save(receipt)
    receipt['_id'] = str(receipt['_id'])
    receipt['user'] = str(receipt['user'])
    return receipt

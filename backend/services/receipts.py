from backend.extensions import mongo
from bson.objectid import ObjectId
from datetime import datetime

# print(mongo)


def add(product_name, number_of_products, me, price):
    receipts = mongo.db.receipts
    users = mongo.db.users
    user = users.find_one({'token': me})

    new_receipt = {'product': product_name, 'number': number_of_products,
                   'user': ObjectId(user['_id']), 'price': price, 'date': datetime.now()}

    receipts.insert(new_receipt)

    return new_receipt


def get_list(me=None):
    receipts = mongo.db.receipts
    records = []
    if me:
        users = mongo.db.users
        user = users.find_one({'token': me})
        records = receipts.find()
    records = receipts.find()
    return [record for record in records]

from datetime import date
import pymongo
from backend.extensions import mongo
import time


def addNew(name, price, count, soldCount, category = None, img = None):
    products = mongo.db.products
    existingProd = products.find_one({'name': name})

    if existingProd:
        raise Exception('Product already exists!')
    
    if not category:
        categories = mongo.db.categories
        category = categories.find_one({'default': True})['name']
    newProduct = {'name': name, 'category': category, 'price': int(price), 'remainingCount': int(count), 'soldCount': int(soldCount), 'timestamp': int(time.time()), 'image': img}
    products.insert(newProduct)

    return True

def edit(currName, newName = None, newCategory = None, newCount = None, newPrice = None, newImg = None):
    products = mongo.db.products
    product = products.find_one({'name': currName})

    if not product:
        raise Exception("Product doesn't exists!")

    if newName:
        product['name'] = newName
    if newCategory:
        categories = mongo.db.categories
        existingCategory = categories.find_one({'name': newCategory})
        
        if not existingCategory:
            raise Exception("Invalid category!")
        product['category'] = newCategory

    if newPrice:
        product['price'] = int(newPrice)
    if newImg:
        product['img'] = newImg
    if newCount:
        product["remainingCount"] = int(newCount)
    
    products.save(product)
        
    return True
    
def get_list(category = None, priceAscending = None, priceDescending = None, date = None, priceRangeMin = None, priceRangeMax = None):
    products = mongo.db.products
    
    filter = [("soldCount", pymongo.DESCENDING)]
    if category:
        records = products.find({'category': category})
    elif priceRangeMax and priceRangeMin:
        print(priceRangeMax, priceRangeMin)
        records = products.find({'price': {'$gte': int(priceRangeMin), '$lte': int(priceRangeMax)}})
    else:
        if priceAscending:
            filter = [("price", pymongo.ASCENDING)]
        elif priceDescending:
            filter = [("price", pymongo.DESCENDING)]
        elif date:
            filter = [("timestamp", pymongo.DESCENDING)]

        records = products.find().sort(filter)
        
    output = []
    for record in records:
        record['_id'] = str(record['_id'])
        output.append(record)
    return output


 

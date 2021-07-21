from backend.extensions import mongo


def addNew(name, category, price, remainingCount, soldCount, img):
    products = mongo.db.products
    existingProd = products.find_one({'name': name})

    if existingProd:
        raise Exception('Product already eists!')
    
    newProduct = {'name': name, 'category': category, 'price': price, 'remainingCount': remainingCount, 'soldCount': soldCount, 'image': img}
    products.insert(newProduct)

    return True


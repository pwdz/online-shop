from backend.extensions import mongo


def addNew(name, category, price, count, soldCount=0, img=None):
    products = mongo.db.products
    existingProd = products.find_one({'name': name})

    if existingProd:
        raise Exception('Product already exists!')

    newProduct = {'name': name, 'category': category, 'price': price,
                  'remainingCount': count, 'soldCount': soldCount, 'image': img}
    products.insert(newProduct)

    return True


def update_category(product_name):
    products = mongo.db.products
    categories = mongo.db.categories

    default_category = categories.find_one({'default': True})
    product = products.find_one({'name': product_name})

    if product is None:
        raise Exception('Product is not found')

    product['category'] = default_category['name']
    products.save(product)
    product['_id'] = str(product['_id'])

    return product


def edit(currName, newName=None, newCategory=None, newCount=None, newPrice=None, newImg=None):
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
        product['price'] = newPrice
    if newImg:
        product['img'] = newImg
    if newCount:
        product["remainingCount"] = newCount

    products.save(product)

    return True

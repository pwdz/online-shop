from backend.extensions import mongo
import backend.services.categories as categoryService


def addNew(name, price, count, soldCount=0, category=None, img=None):
    products = mongo.db.products
    existingProd = products.find_one({'name': name})

    if existingProd:
        raise Exception('Product already exists!')

    if not category:
        categories = mongo.db.categories
        category = categories.find_one({'default': True})['name']
    else:
        if not categoryService.exists(category):
            raise Exception('Category is not found')

    newProduct = {'name': name, 'category': category, 'price': int(
        price), 'remainingCount': int(count), 'soldCount': int(soldCount), 'image': img}

    products.insert(newProduct)

    return True


def update_category(product_name, category_name=None):
    products = mongo.db.products
    categories = mongo.db.categories
    category = []
    product = products.find_one({'name': product_name})

    if product is None:
        raise Exception('Product is not found')
    if category_name:
        print("aloooooooooooo", category_name)
        product['category'] = category_name
    else:
        category = categories.find_one({'default': True})
        product['category'] = category['name']

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
        if not categoryService.exists(newCategory):
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


def get_list():
    products = mongo.db.products
    records = products.find()
    output = []
    for record in records:
        record['_id'] = str(record['_id'])
        output.append(record)
    return output

    return True

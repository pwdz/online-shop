from backend.extensions import mongo


def addNew(name, category, price, remainingCount, soldCount, img):
    products = mongo.db.products
    existingProd = products.find_one({'name': name})

    if existingProd:
        raise Exception('Product already eists!')
    
    newProduct = {'name': name, 'category': category, 'price': price, 'remainingCount': remainingCount, 'soldCount': soldCount, 'image': img}
    products.insert(newProduct)

    return True

def edit(currName, newName = None, newCategory = None, newPrice = None, newImg = None):
    products = mongo.db.products
    product = products.find_one({'name': currName})

   
    if not product:
        raise Exception("Product doesn't exists!")

    if newName:
        product['name'] = newName
    if newCategory:
        categories = mongo.db.categories
        if categories.find({'name': newCategory}) == None:
            raise Exception("Invalid category!")
        product['category'] = newCategory
    if newPrice:
        product['price'] = newPrice
    if newImg:
        product['img'] = newImg
    
    products.save(product)
        
    return True
    

 

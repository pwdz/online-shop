from backend.extensions import mongo
from backend.settings import SECRET_KEY
import backend.services.products as productService


def add_new(name, default=False):
    categories = mongo.db.categories
    new_category = {'name': name, 'default': default}
    existing_category = categories.find_one({'name': name})

    if existing_category is not None:
        existing_category['_id'] = str(existing_category['_id'])
        return existing_category

    categories.insert(new_category)
    new_category['_id'] = str(new_category['_id'])
    return new_category


def edit(cat_name, new_name=None):
    categories = mongo.db.categories

    category = categories.find_one({'name': cat_name})

    if category is None:
        raise Exception('Category is not found!')

    if new_name:
        category["name"] = new_name

    categories.save(category)
    category['_id'] = str(category['_id'])
    return True


def get_list():
    categories = mongo.db.categories
    records = categories.find()
    output = []
    for record in records:
        record['_id'] = str(record['_id'])
        output.append(record)
    return output


def remove(name):
    categories = mongo.db.categories
    products = mongo.db.products
    record = categories.find_one({'name': name})
    if record is None:
        raise Exception('Category is not found')
    if record['default'] is True:
        raise Exception("Default category can't be removed")

    product_records = products.find({'category': record['name']})
    for product_record in product_records:
        productService.update_category(product_record['name'])

    categories.remove(record)
    record['_id'] = str(record['_id'])

    return record


def exists(name):
    categories = mongo.db.categories
    record = categories.find_one({'name': name})

    if record:
        return True
    else:
        return False

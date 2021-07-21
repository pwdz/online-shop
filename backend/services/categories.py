from backend.extensions import mongo
from backend.settings import SECRET_KEY


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


def edit(name=None):
    categories = mongo.db.categories

    category = categories.find_one({'name': name})

    if category is None:
        raise Exception('Category is not found!')

    if name:
        category["name"] = name

    categories.save(category)
    categories['_id'] = str(categories['_id'])
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
    record = categories.find_one({'name': name})
    if record is None:
        raise Exception('Category is not found')
    if record['default'] is True:
        raise Exception("Default category can't be removed")

    categories.remove(record)
    record['_id'] = str(record['_id'])

    return record

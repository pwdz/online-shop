from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import jwt
from bson.objectid import ObjectId


def addNew(name, default=False):
    categories = mongo.db.categories
    new_category = {'name': name, 'default': default}
    existing_category = categories.find_one({'name': name})

    if existing_category is not None:
        return existing_category

    categories.insert(new_category)

    return new_category


def edit(name=None):
    categories = mongo.db.categories

    category = categories.find_one({'name': name})

    if category is None:
        raise Exception('Category is not found!')

    if name:
        category["name"] = name

    categories.save(category)

    return True


def get_list():
    categories = mongo.db.categories
    records = categories.find()
    return [record for record in records]

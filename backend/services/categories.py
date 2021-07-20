from backend.extensions import mongo
import bcrypt
from backend.settings import SECRET_KEY
import jwt
from bson.objectid import ObjectId


def addNew(name, default=False):
    categories = mongo.db.categories
    newCategory = {'name': name, 'default': default}
    existing_category = categories.find_one({'name': name})

    if existing_category is not None:
        raise Exception('Category already exists!')

    categories.insert(newCategory)

    return True


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

# from typing_extensions import Required
from marshmallow import Schema, fields

class AddProductInput(Schema):
    name = fields.Str(required=True)
    category = fields.Str(required=False)
    price = fields.Int(required=True)
    count = fields.Int(required=True)
    
class EditProductInput(Schema):
    name = fields.Str(required=True)
    new_name = fields.Str(required=False)
    new_category = fields.Str(required=False)
    new_price = fields.Int(required=False)
    new_count = fields.Int(required=False)

class GetProductInput(Schema):
    category = fields.Str(required=False)
    price_descending = fields.Bool(required=False)
    price_ascending = fields.Bool(required=False)
    date = fields.Bool(requied=False)   
    price_range_min = fields.Int(required=False)
    price_range_max = fields.Int(required=False)
    name = fields.Str(required=False)
    
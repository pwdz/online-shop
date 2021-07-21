from marshmallow import Schema, fields

class AddProductInput(Schema):
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Int(required=True)
    count = fields.Int(required=True)
    
class EditProductInput(Schema):
    name = fields.Str(required=True)
    new_name = fields.Str(required=False)
    new_category = fields.Str(required=False)
    new_price = fields.Int(required=False)
    new_count = fields.Int(required=False)
 
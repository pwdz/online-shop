from marshmallow import Schema, fields


class RegisterInput(Schema):
    # the 'required' argument ensures the field exists
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=False)
    lastname = fields.Str(required=False)
    address = fields.Str(required=False)

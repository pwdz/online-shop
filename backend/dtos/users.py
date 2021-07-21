from marshmallow import Schema, fields


class RegisterInput(Schema):
    # the 'required' argument ensures the field exists
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=False)
    lastname = fields.Str(required=False)
    address = fields.Str(required=False)


class EditInput(Schema):
    # the 'required' argument ensures the field exists
    password = fields.Str(required=False)
    name = fields.Str(required=False)
    lastname = fields.Str(required=False)
    address = fields.Str(required=False)


class LoginInput(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class IncreaseBalance(Schema):
    balance = fields.Int(required=False)

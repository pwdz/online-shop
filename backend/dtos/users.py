from marshmallow import Schema, fields
from marshmallow.validate import Length, Range, Regexp


class RegisterInput(Schema):
    # the 'required' argument ensures the field exists
    email = fields.Str(required=True, validate=Regexp(
        "[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"))
    password = fields.Str(required=True, validate=[Length(max=255, min=8), Regexp(
        "^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)[0-9a-zA-Z]{8,255}$")])
    name = fields.Str(required=False, validate=Length(max=255))
    lastname = fields.Str(required=False, validate=Length(max=255))
    address = fields.Str(required=False, validate=Length(max=255))


class EditInput(Schema):
    # the 'required' argument ensures the field exists
    password = fields.Str(required=True, validate=[Length(max=255, min=8), Regexp(
        "^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)[0-9a-zA-Z]{8,255}$")])
    name = fields.Str(required=False, validate=Length(max=255))
    lastname = fields.Str(required=False, validate=Length(max=255))
    address = fields.Str(required=False, validate=Length(max=255))


class LoginInput(Schema):
    email = fields.Str(required=True, validate=Regexp(
        "[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"))
    password = fields.Str(required=True, validate=[Length(max=255, min=8), Regexp(
        "^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)[0-9a-zA-Z]{8,255}$")])


class IncreaseBalance(Schema):
    balance = fields.Int(required=False)

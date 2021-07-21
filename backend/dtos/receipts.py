from marshmallow import Schema, fields, validate, ValidationError


class ChangeInput(Schema):
    # the 'required' argument ensures the field exists
    id = fields.Str(required=True)
    state = fields.Str(validate=validate.OneOf(
        ["processing", "processed", "canceled"]))

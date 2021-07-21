from marshmallow import Schema, fields


class AddInput(Schema):
    # the 'required' argument ensures the field exists
    name = fields.Str(required=True)

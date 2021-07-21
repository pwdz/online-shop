from marshmallow import Schema, fields


class AddInput(Schema):
    # the 'required' argument ensures the field exists
    name = fields.Str(required=True)


class EditInput(Schema):
    # the 'required' argument ensures the field exists
    catName = fields.Str(required=True)
    newName = fields.Str(required=False)


class RemoveInput(Schema):
    # the 'required' argument ensures the field exists
    name = fields.Str(required=True)

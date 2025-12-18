from marshmallow import Schema, fields

class MahasiswaSchema(Schema):
    id = fields.Int(dump_only=True)
    nim = fields.Str(required=True)
    nama = fields.Str(required=True)
    jurusan = fields.Str(allow_none=True)
    angkatan = fields.Int(allow_none=True)
    email = fields.Email(allow_none=True)

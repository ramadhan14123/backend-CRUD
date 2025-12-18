from models.models import db, Mahasiswa
from schemas import MahasiswaSchema

mahasiswa_schema = MahasiswaSchema()
mahasiswas_schema = MahasiswaSchema(many=True)

def get_all_mahasiswa():
    mhs = Mahasiswa.query.all()
    return mahasiswas_schema.dump(mhs)

def get_mahasiswa_by_id(mahasiswa_id):
    return Mahasiswa.query.get(mahasiswa_id)

def create_mahasiswa(data):
    errors = mahasiswa_schema.validate(data)
    if errors:
        return {'errors': errors}, 400
    m = Mahasiswa(**data)
    db.session.add(m)
    db.session.commit()
    return mahasiswa_schema.dump(m)

def update_mahasiswa(m, data):
    errors = mahasiswa_schema.validate(data)
    if errors:
        return {'errors': errors}, 400
    for key, value in data.items():
        if hasattr(m, key):
            setattr(m, key, value)
    db.session.commit()
    return mahasiswa_schema.dump(m)

def delete_mahasiswa(m):
    db.session.delete(m)
    db.session.commit()
    return True

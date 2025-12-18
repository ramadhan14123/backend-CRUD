from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy db instance (will be initialized in app)
db = SQLAlchemy()

class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(120), nullable=False)
    jurusan = db.Column(db.String(120))
    angkatan = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f"<Mahasiswa {self.id} {self.nim} {self.nama}>"

# Flask RESTful CRUD Example

Simple CRUD backend using Flask, Flask-RESTful, Flask-SQLAlchemy and Marshmallow.

Files:
- `app.py` - app factory and entrypoint
- `models.py` - SQLAlchemy models
- `schemas.py` - Marshmallow schemas
- `controllers.py` - business logic (CRUD)
- `routes.py` - RESTful resources / endpoints
- `config.py` - config (SQLite URI)

Setup:

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

API endpoints (Mahasiswa):
- GET /mahasiswa
- POST /mahasiswa {nim, nama, jurusan, angkatan, email}
- GET /mahasiswa/<id>
- PUT /mahasiswa/<id>
- DELETE /mahasiswa/<id>


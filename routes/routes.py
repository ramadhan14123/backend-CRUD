from flask import request
from flask_restful import Resource
import controllers.controllers as controllers

class MahasiswaListResource(Resource):
    def get(self):
        return controllers.get_all_mahasiswa(), 200

    def post(self):
        data = request.get_json() or {}
        res = controllers.create_mahasiswa(data)
        if isinstance(res, tuple):
            return res
        return res, 201


class MahasiswaResource(Resource):
    def get(self, mahasiswa_id):
        m = controllers.get_mahasiswa_by_id(mahasiswa_id)
        if not m:
            return {'message': 'Mahasiswa not found'}, 404
        return controllers.mahasiswa_schema.dump(m), 200

    def put(self, mahasiswa_id):
        m = controllers.get_mahasiswa_by_id(mahasiswa_id)
        if not m:
            return {'message': 'Mahasiswa not found'}, 404
        data = request.get_json() or {}
        res = controllers.update_mahasiswa(m, data)
        if isinstance(res, tuple):
            return res
        return res, 200

    def delete(self, mahasiswa_id):
        m = controllers.get_mahasiswa_by_id(mahasiswa_id)
        if not m:
            return {'message': 'Mahasiswa not found'}, 404
        controllers.delete_mahasiswa(m)
        return '', 204


def register_routes(api):
    api.add_resource(MahasiswaListResource, '/mahasiswa')
    api.add_resource(MahasiswaResource, '/mahasiswa/<int:mahasiswa_id>')

from flask import request
from flask_restx import Namespace, Resource
from container import director_service
from app.dao.model.director_model import DirectorSchema
from decorators import auth_reguired, admin_reguired

director_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route("/")
class DirectorsView(Resource):
    @auth_reguired
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200

    @admin_reguired
    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201

@director_ns.route("/<int:did>")
class DirectorView(Resource):
    @auth_reguired
    def get(self, did):
        return director_schema.dump(director_service.get_one(did)), 200

    @admin_reguired
    def put(self):
        req_json = request.json
        director_service.update(req_json)
        return "", 204

    @admin_reguired
    def delete(self, did):
        director_service.delete(did)
        return "", 204
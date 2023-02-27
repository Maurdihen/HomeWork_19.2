from flask import request
from flask_restx import Namespace, Resource
from container import genre_service
from app.dao.model.genre_model import GenreSchema
from decorators import auth_reguired
from decorators import admin_reguired

genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route("/")
class GenresView(Resource):
    @auth_reguired
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200

    @admin_reguired
    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201


@genres_ns.route("/<int:gid>")
class GenreView(Resource):
    @auth_reguired
    def get(self, gid):
        return genre_schema.dump(genre_service.get_one(gid)), 200

    @admin_reguired
    def put(self):
        req_json = request.json
        genre_service.update(req_json)
        return "", 204

    @admin_reguired
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204

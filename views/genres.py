from flask_restx import Namespace, Resource
from container import genre_service
from dao.model.genre_model import GenreSchema

genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200


@genres_ns.route("/<int:fid>")
class GenreView(Resource):
    def get(self, fid):
        return genre_schema.dump(genre_service.get_one(fid)), 200

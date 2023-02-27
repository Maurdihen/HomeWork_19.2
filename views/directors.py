from flask_restx import Namespace, Resource
from container import director_service
from dao.model.director_model import DirectorSchema

director_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200

@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        return director_schema.dump(director_service.get_one(did)), 200
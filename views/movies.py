from flask_restx import Namespace, Resource
from container import movie_service
from dao.model.movie_model import MovieSchema
from flask import request

import json

film_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@film_ns.route("/")
class FilmsView(Resource):
    def get(self):
        genres_args = request.args.get("genre_id", False)
        director_args = request.args.get("director_id", False)
        year_args = request.args.get("year", False)
        return movies_schema.dump(movie_service.get_all(genres_args, director_args, year_args)), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201

@film_ns.route("/<int:fid>")
class FilmView(Resource):
    def get(self, fid):
        return movie_schema.dump(movie_service.get_one(fid)), 200

    def put(self, fid):
        req_json = request.json
        movie_service.update(req_json)
        return "", 204

    def delete(self, fid):
        movie_service.delete(fid)
        return "", 204

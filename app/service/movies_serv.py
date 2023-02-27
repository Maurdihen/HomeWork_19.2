from dao.movies_dao import MovieDao
from flask import request

class MovieServise:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_all(self, genres_args, director_args, year_args):
        if director_args and genres_args:
            return list(set(self.dao.get_by_director(director_args)) & set(self.dao.get_by_genre(genres_args)))
        elif director_args:
            return self.dao.get_by_director(director_args)
        elif genres_args:
            return self.dao.get_by_genre(genres_args)
        elif year_args:
            return self.dao.get_by_year(year_args)
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.dao.get_by_genre(gid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data["id"]
        movie = self.get_one(mid)

        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]

        return self.dao.update(movie)

    def update_partial(self, data):
        mid = data["id"]
        movie = self.get_one(mid)

        if data["title"]:
            movie.title = data["title"]
        if data["description"]:
            movie.description = data["description"]
        if data["trailer"]:
            movie.trailer = data["trailer"]
        if data["year"]:
            movie.year = data["year"]
        if data["rating"]:
            movie.rating = data["rating"]
        if data["genre_id"]:
            movie.genre_id = data["genre_id"]
        if data["director_id"]:
            movie.director_id = data["director_id"]

        return self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)

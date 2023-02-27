from dao.model.movie_model import Movie

class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        self.session.delete(self.session.query(Movie).get(mid))
        self.session.commit()

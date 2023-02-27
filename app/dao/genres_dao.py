from dao.model.genre_model import Genre

class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, aid):
        return self.session.query(Genre).get(aid)
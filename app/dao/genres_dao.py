from app.dao.model.genre_model import Genre

class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def create(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        self.session.delete(self.session.query(Genre).get(gid))
        self.session.commit()
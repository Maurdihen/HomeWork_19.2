from dao.model.genre_model import Genre

class GenreServise:
    def __init__(self, dao: Genre):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)
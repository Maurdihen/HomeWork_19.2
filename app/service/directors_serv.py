from app.dao.model.director_model import Director

class DirectorServise:
    def __init__(self, dao: Director):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)
from dao.model.director_model import Director

class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, aid):
        return self.session.query(Director).get(aid)
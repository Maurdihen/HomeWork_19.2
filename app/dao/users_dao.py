from app.dao.model.user_model import User

class UserDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        self.session.delete(self.session.query(User).get(uid))
        self.session.commit()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

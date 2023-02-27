import base64
import hashlib
import hmac

from app.dao.users_dao import UserDao
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        uid = data["id"]
        user = self.get_one(uid)

        user.username = data["username"]
        user.password = data["password"]
        user.role = data["role"]

        return self.dao.update(user)

    def update_partial(self, data):
        uid = data["id"]
        user = self.get_one(uid)

        if data["username"]:
            user.username = data["username"]
        if data["password"]:
            user.password = data["password"]
        if data["trailer"]:
            user.trailer = data["trailer"]
        if data["role"]:
            user.role = data["role"]

        return self.dao.update(user)

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def compare_password(self, password_hash, other_password):
        decoded_digist = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digist, hash_digest)
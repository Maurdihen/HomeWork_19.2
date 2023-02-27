from app.dao.movies_dao import MovieDao
from app.dao.directors_dao import DirectorDao
from app.dao.genres_dao import GenreDao
from app.service.directors_serv import DirectorServise
from app.service.genres_serv import GenreServise
from app.service.movies_serv import MovieServise
from app.service.users_serv import UserService
from app.dao.users_dao import UserDao
from app.service.auth_serv import AuthService
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieServise(dao=movie_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreServise(dao=genre_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorServise(dao=director_dao)

user_dao = UserDao(db.session)
user_service = UserService(dao=user_dao)

auth_service = AuthService(user_service)
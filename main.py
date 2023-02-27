from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.genres import genres_ns
from views.movies import film_ns
from views.directors import director_ns
from views.users import user_ns
from views.auth import auth_ns


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    configure_app(app)

    return app

def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genres_ns)
    api.add_namespace(film_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


if __name__ == "__main__":
    app = create_app(Config)
    app.run(debug=True,port=5001)
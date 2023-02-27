from setup_db import db
from marshmallow import Schema, fields

class Genre(db.Model):
    __tablename__ = "genre"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
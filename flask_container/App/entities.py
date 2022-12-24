from flask_login import UserMixin
from sqlalchemy import String

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return f'<User "{self.name}">'


class Computation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    input_image = db.Column(String)
    denoised_image = db.Column(String)
    extracted_text = db.Column(String)

    def __repr__(self):
        return f'<Computation "{self.extracted_text[:20]}">'

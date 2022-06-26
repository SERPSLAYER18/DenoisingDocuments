from . import db
from flask_login import UserMixin


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
    input_image = db.Column(db.String(500000))
    denoised_image = db.Column(db.String(500000))
    extracted_text = db.Column(db.String(500))

    def __repr__(self):
        return f'<Computation "{self.extracted_text[:20]}">'
